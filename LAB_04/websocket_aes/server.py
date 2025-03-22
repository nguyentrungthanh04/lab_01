import tornado.ioloop
import tornado.web
import tornado.websocket
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import base64

class WebSocketServer(tornado.websocket.WebSocketHandler):
    def open(self):
        print("Client connected")

        # Tạo khóa AES 16 byte và gửi cho client
        self.aes_key = get_random_bytes(16)
        self.write_message(base64.b64encode(self.aes_key).decode())

        print(f"Sent AES key to client: {self.aes_key.hex()}")

    def on_message(self, message):
        if not message:
            print("Received empty message from client.")
            return

        print(f"Received from client: {message}")

        # Mã hóa tin nhắn bằng AES
        cipher = AES.new(self.aes_key, AES.MODE_CBC)
        ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
        encrypted_message = base64.b64encode(cipher.iv + ciphertext).decode()

        print(f"Sending encrypted message: {encrypted_message}")
        self.write_message(encrypted_message)

    def on_close(self):
        print("Client disconnected")

def make_app():
    return tornado.web.Application([(r"/websocket", WebSocketServer)])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("WebSocket server running on ws://localhost:8888/websocket")
    tornado.ioloop.IOLoop.current().start()
