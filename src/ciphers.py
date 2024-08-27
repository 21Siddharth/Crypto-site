import base64

def caesar_cipher(text, shift, encode_numbers=False):
    encoded_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encoded_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encoded_text += encoded_char
        elif encode_numbers and char.isdigit():
            encoded_char = chr((ord(char) - 48 + shift) % 10 + 48)
            encoded_text += encoded_char
        else:
            encoded_text += char
    return encoded_text

def caesar_decipher(encoded_text, shift, encode_numbers=False):
    return caesar_cipher(encoded_text, -shift, encode_numbers)

def rot13(text, rotate_uppercase=True, rotate_lowercase=True, rotate_numbers=False):
    result = ""
    for char in text:
        if rotate_uppercase and 'A' <= char <= 'Z':
            result += chr((ord(char) - 65 + 13) % 26 + 65)
        elif rotate_lowercase and 'a' <= char <= 'z':
            result += chr((ord(char) - 97 + 13) % 26 + 97)
        elif rotate_numbers and '0' <= char <= '9':
            result += chr((ord(char) - 48 + 5) % 10 + 48)
        else:
            result += char
    return result

def base64_encode(text):
    message_bytes = text.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message

def base64_decode(base64_text):
    base64_bytes = base64_text.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    return message
