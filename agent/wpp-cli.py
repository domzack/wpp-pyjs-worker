from PIL import Image
import socketio
import base64
from io import BytesIO
import sys
import matplotlib.pyplot as plt  # Adicione este import
import queue

from agent_lanchonete import processar_mensagem_whatsapp  # Importe aqui


# Cria uma instância do cliente Socket.IO
sio = socketio.Client()

img_queue = queue.Queue()


@sio.event
def connect():
    print("Conectado ao servidor!")


@sio.event
def disconnect():
    print("Desconectado do servidor!")


@sio.on("qrcode")
def on_qrcode(data):
    print("QR Code recebido!")
    # Decodifica o base64 para bytes
    img_bytes = base64.b64decode(data.split(",")[1] if "," in data else data)
    # Cria imagem a partir dos bytes e adiciona à fila
    img = Image.open(BytesIO(img_bytes))
    img_queue.put(img)


@sio.on("status")
def on_status(data):
    print("Status da sessão:", data)


@sio.on("message")
def on_message(data):
    # Espera que data seja um dict com id, name, shortname, body

    remetente = data.get("from")
    sender = data.get("sender")
    shortname = sender.get("shortName") if sender else "_undefined_"
    body = data.get("body")

    if remetente.endswith("@c.us"):
        print(f"\nMensagem recebida de {remetente} ({shortname})")
        print("Mensagem recebida:", body)
        print("----------\n")

        resposta = processar_mensagem_whatsapp(remetente, shortname, body)
        sio.emit("send-message", {"message": resposta, "to": remetente})
        print(f"Atendente: {resposta}")


@sio.on("error")
def on_error(data):
    print("Erro:", data)
    # Não encerre o programa aqui


def main():
    sio.connect("http://localhost:3000")
    sio.emit("create-session", {"sessionName": "minha_sessao"})
    try:
        while True:
            try:
                img = img_queue.get(timeout=1)
                plt.imshow(img)
                plt.axis("off")
                plt.title("QR Code")
                plt.show()
            except queue.Empty:
                pass
            sio.sleep(0.1)
    except KeyboardInterrupt:
        print("Encerrando por Ctrl+C...")
        sio.disconnect()
        sys.exit(0)


if __name__ == "__main__":
    main()
