from flask import Flask, render_template, request, jsonify
from ciphers import caesar_cipher, caesar_decipher, rot13, base64_encode, base64_decode

app = Flask(__name__, static_folder='Frontend', static_url_path='/Frontend', template_folder='Frontend/page')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encode', methods=['POST'])
def encode():
    data = request.json
    text = data.get('text')
    shift = int(data.get('shift', 0))
    method = data.get('method')
    encode_numbers_caesar = data.get('encodeNumbersCaesar', False)

    rotate_uppercase = data.get('rotateUppercase', False)
    rotate_lowercase = data.get('rotateLowercase', False)
    rotate_numbers = data.get('rotateNumbers', False)

    if method == 'caesar':
        encoded_text = caesar_cipher(text, shift, encode_numbers_caesar)
    elif method == 'rot13':
        encoded_text = rot13(text, rotate_uppercase, rotate_lowercase, rotate_numbers)
    elif method == 'base64':
        encoded_text = base64_encode(text)
    else:
        encoded_text = text

    return jsonify({'encoded_text': encoded_text})

@app.route('/decode', methods=['POST'])
def decode():
    data = request.json
    text = data.get('text')
    shift = int(data.get('shift', 0))
    method = data.get('method')
    encode_numbers_caesar = data.get('encodeNumbersCaesar', False)

    rotate_uppercase = data.get('rotateUppercase', False)
    rotate_lowercase = data.get('rotateLowercase', False)
    rotate_numbers = data.get('rotateNumbers', False)

    if method == 'caesar':
        decoded_text = caesar_decipher(text, shift, encode_numbers_caesar)
    elif method == 'rot13':
        decoded_text = rot13(text, rotate_uppercase, rotate_lowercase, rotate_numbers)
    elif method == 'base64':
        decoded_text = base64_decode(text)
    else:
        decoded_text = text

    return jsonify({'decoded_text': decoded_text})

if __name__ == '__main__':
    app.run(debug=True)