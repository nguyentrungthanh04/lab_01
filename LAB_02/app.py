from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher
from cipher.playfair import PlayFairCipher
from cipher.railfence import RailFenceCipher
from cipher.transposition import TranspositionCipher
from cipher.Vigenere import VigenereCipher
import re 

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

# ------------------ CAESAR CIPHER ------------------
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/caesar/encrypt", methods=['POST'])
def caesar_encrypt():
    try:
        text = request.form['inputPlainText']
        key = int(request.form['inputKeyPlain'])
        Caesar = CaesarCipher()
        encrypted_text = Caesar.encrypted_text(text, key)
        return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"
    except ValueError:
        return "Invalid Key! Please enter a number."

@app.route("/caesar/decrypt", methods=['POST'])
def caesar_decrypt():
    try:
        text = request.form['inputCipherText']
        key = int(request.form['inputKeyCipher'])
        Caesar = CaesarCipher()
        decrypted_text = Caesar.decrypted_text(text, key)
        return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"
    except ValueError:
        return "Invalid Key! Please enter a number."

# ------------------ PLAYFAIR CIPHER ------------------
@app.route("/playfair")
def playfair():
    return render_template('playfair.html')

def generate_playfair_matrix(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key = "".join(dict.fromkeys(key.upper().replace("J", "I")))  
    matrix_str = key + "".join(c for c in alphabet if c not in key)
    matrix = [list(matrix_str[i:i+5]) for i in range(0, 25, 5)]
    
    # In ma trận để kiểm tra
    print("Generated Playfair Matrix:")
    for row in matrix:
        print(" ".join(row))
    
    return matrix if len(matrix) == 5 else None

@app.route("/playfair/matrix", methods=['POST'])
def playfair_matrix():
    key = request.form['inputKeyPlain'].replace(" ", "").upper()
    if not re.match("^[A-Z]+$", key):
        return "Invalid Key! Only alphabets are allowed.", 400
    PlayFair = PlayFairCipher()
    matrix = PlayFair.create_playfair_matrix(key)
    return render_template('playfair.html', matrix=matrix)

@app.route("/playfair/encrypt", methods=['POST'])
def playfair_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    PlayFair = PlayFairCipher()
    matrix = PlayFair.create_playfair_matrix(key) 
    encrypted_text = PlayFair.playfair_encrypt(text, matrix) 
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/playfair/decrypt", methods=['POST'])
def playfair_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    PlayFair = PlayFairCipher()
    matrix = PlayFair.create_playfair_matrix(key)
    decrypted_text = PlayFair.playfair_decrypt(text, matrix)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

# ------------------ RAIL FENCE CIPHER ------------------
@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route("/railfence/encrypt", methods=['POST'])
def railfence_encrypt():
    try:
        text = request.form['inputPlainText']
        key = int(request.form['inputKeyPlain'])
        RailFence = RailFenceCipher()
        encrypted_text = RailFence.rail_fence_encrypt(text, key)
        return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"
    except ValueError:
        return "Invalid Key! Please enter a number."

@app.route("/railfence/decrypt", methods=['POST'])
def railfence_decrypt():
    try:
        text = request.form['inputCipherText']
        key = int(request.form['inputKeyCipher'])
        RailFence = RailFenceCipher()
        decrypted_text = RailFence.rail_fence_decrypt(text, key)
        return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"
    except ValueError:
        return "Invalid Key! Please enter a number."

# ------------------ TRANSPOSITION CIPHER ------------------
@app.route("/transposition")
def transposition():
    return render_template('transposition.html')

@app.route("/transposition/encrypt", methods=['POST'])
def transposition_encrypt():
    try:
        text = request.form['inputPlainText']
        key = int(request.form['inputKeyPlain'])
        Transposition = TranspositionCipher()
        encrypted_text = Transposition.encrypt(text, key)
        return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"
    except ValueError:
        return "Invalid Key! Please enter a number."

@app.route("/transposition/decrypt", methods=['POST'])
def transposition_decrypt():
    try:
        text = request.form['inputCipherText']
        key = int(request.form['inputKeyCipher'])
        Transposition = TranspositionCipher()
        decrypted_text = Transposition.decrypt(text, key)
        return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"
    except ValueError:
        return "Invalid Key! Please enter a number."

# ------------------ VIGENERE CIPHER ------------------
@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/vigenere/encrypt", methods=['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    Vigenere = VigenereCipher()
    encrypted_text = Vigenere.vigenere_encrypted(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/vigenere/decrypt", methods=['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    Vigenere  = VigenereCipher()
    decrypted_text = Vigenere.vigenere_decrypted(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
