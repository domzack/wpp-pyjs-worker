# WPPConnect Server

Servidor Express com EJS para integração com o WhatsApp via [WPPConnect](https://github.com/wppconnect-team/wppconnect).

## Funcionalidades

- Criação e gerenciamento de múltiplas sessões WhatsApp via WebSocket.
- Geração e exibição de QR Code para autenticação.
- Interface web estilizada e responsiva.
- Encerramento de sessões pelo navegador.
- Busca automática do caminho do Chrome instalado no sistema.

## Requisitos

- Node.js >= 18
- Google Chrome ou Chromium instalado

## Instalação

1. Clone o repositório:
    ```sh
    git clone <seu-repo>
    cd wpp
    ```

2. Instale as dependências:
    ```sh
    npm install
    ```

## Uso

### Ambiente de desenvolvimento

```sh
npm run dev
```

### Ambiente de produção

```sh
npm start
```

Acesse [http://localhost:3000](http://localhost:3000) no navegador.

## Estrutura

- `src/server.js`: Servidor Express, Socket.IO e integração WPPConnect.
- `views/index.ejs`: Interface web para criar/encerrar sessões e visualizar QR Code.
- `tokens/`: Pasta onde os tokens das sessões são salvos.

## Principais Endpoints

- `/`: Interface web principal.
- WebSocket: eventos `create-session`, `close-session`, `qrcode`, `status`, `message`, `error`.

## Observações

- O servidor busca automaticamente o caminho do Chrome/Chromium usando o pacote `chrome-launcher`.
- Caso não encontre o navegador, instale o Chrome ou Chromium manualmente.

## Licença

ISC

---

Desenvolvido com [WPPConnect](https://github.com/wppconnect-team/wppconnect) e [Express](https://expressjs.com/).