import tornado.ioloop
import tornado.websocket
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

class WebSocketClient:
    def __init__(self, io_loop):
        self.io_loop = io_loop
        self.connection = None
        self.aes_key = None  # Chờ nhận từ server

    def start(self):
        self.connect()

    def connect(self):
        tornado.websocket.websocket_connect(
            "ws://localhost:8888/websocket",
            callback=self.on_connect
        )

    def on_connect(self, future):
        try:
            self.connection = future.result()
            print("Connected to WebSocket server")

            # Nhận khóa AES từ server
            self.connection.read_message(self.receive_aes_key)
        except Exception as e:
            print(f"Connection failed: {e}")
            self.io_loop.call_later(3, self.connect)

    def receive_aes_key(self, future):
        try:
            aes_key_encoded = future.result()
            if aes_key_encoded is None:
                print("Failed to receive AES key.")
                return

            # Giải mã khóa AES
            self.aes_key = base64.b64decode(aes_key_encoded)
            print(f"Received AES key: {self.aes_key.hex()}")

            # Sau khi nhận khóa AES, cho phép gửi tin nhắn
            self.send_message()
        except Exception as e:
            print(f"Error receiving AES key: {e}")

    def send_message(self):
        message = input("Enter message: ")
        self.connection.write_message(message)

        # Đọc tin nhắn phản hồi
        self.connection.read_message(self.on_message)

    def on_message(self, future):
        try:
            encrypted_message = future.result()  # Lấy dữ liệu từ Future

            if encrypted_message is None:
                print("Disconnected from server.")
                self.connect()
                return

            print(f"Encrypted message from server: {encrypted_message}")

            # Giải mã tin nhắn
            encrypted_bytes = base64.b64decode(encrypted_message)

            if len(encrypted_bytes) < AES.block_size:
                print("Error: Dữ liệu không đủ kích thước!")
                return

            iv = encrypted_bytes[:AES.block_size]
            ciphertext = encrypted_bytes[AES.block_size:]
            cipher = AES.new(self.aes_key, AES.MODE_CBC, iv)
            decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size).decode()

            print(f"Decrypted message: {decrypted_message}")

        except Exception as e:
            print(f"Error in on_message: {e}")

        self.send_message()  # Tiếp tục gửi tin nhắn mới

def main():
    io_loop = tornado.ioloop.IOLoop.current()
    client = WebSocketClient(io_loop)
    io_loop.add_callback(client.start)
    io_loop.start()

if __name__ == "__main__":
    main()
