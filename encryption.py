#for encryption
import base64
from cryptography.fernet import Fernet

def encode(ID):
    flashcard_id_bytes = str(flashcard_id).encode()
    encoded_id = fernet.encrypt(flashcard_id_bytes)
    return base64.urlsafe_b64encode(encoded_id).decode()

def decode(hidden_id):
    secret_key = Fernet.generate_key()
    fernet = Fernet(b'BKbvCDV8Jm-j9AckVLyjNQlFWNE3UYh4y0yivKxEhdI=')
    decoded_id_bytes = base64.urlsafe_b64decode(hidden_id)
    flashcard_id_bytes = fernet.decrypt(decoded_id_bytes)
    return int(flashcard_id_bytes.decode())