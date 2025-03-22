import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.rsa import Ui_RSACipher
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_RSACipher()
        self.ui.setupUi(self)
        self.ui.btn_GenerateKey.clicked.connect(self.call_api_generatekey)
        self.ui.btn_Encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_Decrypt.clicked.connect(self.call_api_decrypt)
        self.ui.btn_Sign.clicked.connect(self.call_api_sign)
        self.ui.btn_Verify.clicked.connect(self.call_api_verify)
        
    def call_api_generatekey(self):
        url = "http://127.0.0.1:5000/api/rsa/generate_keys"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText(data["message"])
                msg.exec_()            
            else:
                print("Error while calling API")      
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e.message)
        
    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/rsa/encrypt"
        payload = {
            "message": self.ui.txt_PlainText.toPlainText(),
            "key_type": "public"
        }    
        try: 
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_CipherText.setPlainText(data["encrypted_message"])
                
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encrypted Successfully")
                msg.exec_()            
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e.message)
            
    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/rsa/decrypt"
        payload = {
            "ciphertext": self.ui.txt_CipherText.toPlainText(),
            "key_type": "private"
        }          
        try: 
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_PlainText.setPlainText(data["decrypted_message"])                
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e.message)
            
    def call_api_sign(self):
        url = "http://127.0.0.1:5000/api/rsa/sign"
        payload = {
            "message": self.ui.txt_Informatin.toPlainText(),
        }        
        try: 
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_Signature.setPlainText(data["signature"])                
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Signed Successfully")
                msg.exec_()              
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e.message)
            
    def call_api_verify(self):
        url = "http://127.0.0.1:5000/api/rsa/verify"
        payload = {
            "message": self.ui.txt_Informatin.toPlainText(),
            "signature": self.ui.txt_Signature.toPlainText()
        }      
        try: 
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                if (data["is_verified"]):               
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Verified Successfully")
                    msg.exec_()
                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Verified Fail")
                    msg.exec_()
            else:        
                print("Error while calling API")
                
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e.message)
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())            
            

