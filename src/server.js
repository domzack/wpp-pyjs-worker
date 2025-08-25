const express = require('express')
const bodyParser = require('body-parser')
const path = require('path')
const http = require('http')
const wpp = require('@wppconnect-team/wppconnect')
const routes = require('./routes')
const cors = require('cors')

const app = express()
const server = http.createServer(app)

const io = require('socket.io')(server, {
    cors: {
        origin: "*",
        methods: ["GET", "POST"]
    },
    allowEIO3: true // Adicione esta linha!
})

app.set('view engine', 'ejs')
app.set('views', path.join(__dirname, '..', 'views'))
app.use(bodyParser.urlencoded({ extended: false }))
app.use(cors())

app.use('/', routes)

let wpp_list = []

io.on('connection', (socket) => {

    socket.on('send-message', ({ message, to }) => {
        const sessionName = socket.sessionName
        const existingSession = wpp_list.find(wpp => wpp.sessionName === sessionName)
        console.log(`Enviando mensagem para ${to} na sessão ${sessionName}:`, message);

        if (existingSession && existingSession.client) {
            // Antes de enviar, verifique se o cliente está conectado e a página está ativa
            existingSession.client.isConnected().then(isConnected => {
                if (!isConnected) {
                    socket.emit('message-error', { to, error: 'Cliente não está conectado. Recarregue a sessão.' })
                    return
                }
                // Tente enviar a mensagem e trate erros de frame detached
                existingSession.client.sendText(to, message)
                    .then(() => {
                        console.log(`Mensagem enviada para ${to}: ${message}`);
                        socket.emit('message-sent', { to, message })
                    })
                    .catch((error) => {
                        // Se for erro de frame detached, tente reiniciar a sessão
                        if (error.message && error.message.includes('detached Frame')) {
                            console.error(`Frame detached detectado. Reiniciando sessão ${sessionName}...`);
                            socket.emit('message-error', { to, error: 'Sessão do WhatsApp ficou inativa. Tente fechar e abrir novamente.' })
                            // Opcional: aqui você pode tentar fechar e reabrir a sessão automaticamente
                        } else {
                            console.error(`Erro ao enviar mensagem para ${to}:`, error);
                            socket.emit('message-error', { to, error: error.message })
                        }
                    })
            }).catch((error) => {
                socket.emit('message-error', { to, error: 'Erro ao verificar conexão do cliente.' })
            })
        } else {
            socket.emit('session-error', { sessionName, error: 'Sessão não encontrada ou cliente não conectado' })
        }
    })

    socket.on('create-session', ({ sessionName }) => {

        socket.sessionName = sessionName

        const cb_events = {
            qrCode: (base64Qrimg) => { socket.emit('qrcode', base64Qrimg) },
            status: (statusSession) => { socket.emit('status', statusSession) },
            message: (message) => { socket.emit('message', message) },
            error: (error) => { socket.emit('error', error) }
        }

        const existingSession = wpp_list.find(wpp => wpp.sessionName === sessionName)
        if (existingSession) {
            existingSession.client.isConnected().then(isConnected => {
                cb_events.status(isConnected ? 'connected' : 'disconnected')
                if (isConnected) {
                    existingSession.client.onMessage(message => cb_events.message(message))
                    existingSession.client.onStateChange(state => {
                        cb_events.status(state)
                        console.log(sessionName, ' | State changed:', state)
                    })
                }

            }).catch((error) => cb_events.error(error))
            return
        }

        const WppSession = getWppSession(sessionName, cb_events)

        WppSession.then((client) => {

            client.onMessage(message => cb_events.message(message))
            client.onStateChange(state => {
                cb_events.status(state)
                console.log(sessionName, ' | State changed:', state)
            })

            wpp_list.push({ sessionName, client })
            socket.emit('session-created', { sessionName })
            console.log(sessionName, ' | Session created successfully')
        }).catch((error) => {
            console.error(sessionName, ' | Error creating session:', error)
            socket.emit('session-error', { sessionName, error: error.message })
        })

    })

    socket.on('close-session', ({ sessionName }) => {
        const Session = wpp_list.find(wpp => wpp.sessionName === sessionName)
        if (Session && Session.client && Session.client.close) {
            Session.client.close().then(() => {
                wpp_list = wpp_list.filter(wpp => wpp.sessionName !== sessionName)
                socket.emit('session-closed', { sessionName })
                console.log(sessionName, ' | Session closed successfully')
            }).catch((error) => {
                console.error(sessionName, ' | Error closing session:', error)
                socket.emit('session-error', { sessionName, error: error.message })
            })

        }

    })
})

server.listen(3000, () => { console.log('Servidor rodando em http://localhost:3000') })

async function getWppSession(sessionName, cb_events) {
    const chromePaths = await require('chrome-launcher').Launcher.getInstallations()
    const chromePath = chromePaths.length > 0 ? chromePaths[0] : null
    return new Promise((resolve, reject) => {
        wpp.create({
            session: sessionName,
            headless: true, // Set to false if you want to see the browser
            logQR: true,    // Set to true to log QR code in console
            debug: false,
            catchQR: (base64Qrimg) => { cb_events.qrCode(base64Qrimg) },
            statusFind: (statusSession) => { cb_events.status(statusSession) },
            folderNameToken: './tokens/',
            useChrome: true,
            browserPath: chromePath,
            browserArgs: ['--no-sandbox'],
            puppeteerOptions: {
                executablePath: chromePath,
                args: ['--no-sandbox', '--disable-setuid-sandbox'],
                defaultViewport: null,
                ignoreHTTPSErrors: true
            }
        })
            .then((client) => {
                resolve(client)
            })
            .catch((error) => { reject(error) })
    })
}