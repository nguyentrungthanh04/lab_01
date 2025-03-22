import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.playfair import Ui_PlayFairCipher  # Import UI từ file playfair.ui
import requests


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_PlayFairCipher()
        self.ui.setupUi(self)
        self.ui.btn_Generate_Matrix.clicked.connect(self.call_api_create_matrix)
        self.ui.btn_Encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_Decrypt.clicked.connect(self.call_api_decrypt)

    def call_api_create_matrix(self):
        key = self.ui.txt_Key.toPlainText()
        if not key:
            QMessageBox.critical(self, "Error", "Key cannot be empty!")
            return

        url = "http://127.0.0.1:5000/api/playfair/creatematrix"
        payload = {"key": key}

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                playfair_matrix = data["playfair_matrix"]


                matrix_str = "\n".join(" ".join(row) for row in playfair_matrix)
            
                self.ui.txt_GenerateMatrix.setPlainText(matrix_str)
                QMessageBox.information(self, "Success", "Matrix created successfully!")
            else:
                QMessageBox.critical(self, "Error", f"Failed to create matrix: {response.text}")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Error: {e}")

    def call_api_encrypt(self):
        plain_text = self.ui.txt_PlainText.toPlainText()
        key = self.ui.txt_Key.toPlainText()
        if not plain_text or not key:
            QMessageBox.critical(self, "Error", "Plain text and key cannot be empty!")
            return

        url = "http://127.0.0.1:5000/api/playfair/encrypt"
        payload = {"plain_text": plain_text, "key": key}

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                encrypted_text = data["encrypted_text"]
                self.ui.txt_CipherText.setPlainText(encrypted_text)
                QMessageBox.information(self, "Success", "Encrypted successfully!")
            else:
                QMessageBox.critical(self, "Error", f"Failed to encrypt: {response.text}")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Error: {e}")

    def call_api_decrypt(self):
        # Gửi yêu cầu giải mã đến API
        cipher_text = self.ui.txt_CipherText.toPlainText()
        key = self.ui.txt_Key.toPlainText()
        if not cipher_text or not key:
            QMessageBox.critical(self, "Error", "Cipher text and key cannot be empty!")
            return

        url = "http://127.0.0.1:5000/api/playfair/decrypt"
        payload = {"cipher_text": cipher_text, "key": key}

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                decrypted_text = data["decrypted"]
                self.ui.txt_PlainText.setPlainText(decrypted_text)
                QMessageBox.information(self, "Success", "Decrypted successfully!")
            else:
                QMessageBox.critical(self, "Error", f"Failed to decrypt: {response.text}")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Error: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())