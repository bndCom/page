from flask import Flask, request, jsonify
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
from secret import FLAG
import os
iv = os.urandom(24)
app = Flask(__name__)

def xor(a, b):
    return bytes(x ^ y for x,y in zip(a, b * (1 + len(a) // len(b))))

@app.route("/encrypt", methods=["GET"])
def encrypt():
    key = request.args.get("key")
    plaintext = request.args.get("plaintext")

    if not key or not plaintext:
        return jsonify({"error": "Key and plaintext are required!"}), 400

    try:
        key_bytes = bytes.fromhex(key)
        plaintext_bytes = xor(bytes.fromhex(plaintext), iv)

        cipher = DES.new(key_bytes, DES.MODE_ECB)

        padded_plaintext = pad(plaintext_bytes, DES.block_size)
        ciphertext = cipher.encrypt(padded_plaintext)

        return jsonify(
            {"ciphertext": ciphertext.hex(), "message": "Encryption successful!"}
        )

    except Exception as e:
        return jsonify({"error": "An error has occurred, most likely due to an incorrect key length."}), 500


@app.route("/encrypt_flag", methods=["GET"])
def encrypt_flag():
    key = request.args.get("key")

    if not key:
        return jsonify({"error": "Key is required!"}), 400

    try:

        key_bytes = bytes.fromhex(key)

        cipher = DES.new(key_bytes, DES.MODE_ECB)

        encrypted_flag = cipher.encrypt(pad(FLAG, 8))
        return jsonify(
            {"flag": xor(encrypted_flag, iv).hex(), "message": "Flag encryption successful!"}
        )

    except Exception as e:
        return jsonify({"error": "An error has occurred, most likely due to an incorrect key length."}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
