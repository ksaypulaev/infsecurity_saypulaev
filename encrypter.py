from cryptography.fernet import Fernet
import rsa
from rsa import PrivateKey, PublicKey


class Encrypter:
    def __init__(self):
        self.key = b''
        self.fernet_key = Fernet(self.key)

        self.public_key, self.private_key = rsa.newkeys(1024)
        self.foreign_public_key = None

    def encrypt(self, message: bytes) -> bytes:
        return self.fernet_key.encrypt(message)

    def decrypt(self, ciphertext: bytes) -> bytes:
        return self.fernet_key.decrypt(ciphertext)

    def do_asym_encrypt(self, message: bytes, public_key: PublicKey) -> bytes:
        return rsa.encrypt(message, public_key)

    def do_asym_decrypt(self, ciphertext: bytes, private_key: PrivateKey) -> bytes:
        return rsa.decrypt(ciphertext, private_key)

    # 
    def get_public_key(self) -> bytes:
        return self.public_key.save_pkcs1("PEM")

    # Инсерт чужого паблик кеу
    def insert_foreign_public_key(self, public_key: bytes):
        self.foreign_public_key = rsa.PublicKey.load_pkcs1(public_key)

    # Расшифровка полученного сообщения
    def do_asym_decrypt_of_foreign_message(self, ciphertext: bytes) -> bytes:
        return self.do_asym_decrypt(ciphertext, self.private_key)
        return rsa.decrypt()
    
    # Шифрование сообщения
    def do_asym_encrypt_of_message(self, text: bytes) -> bytes:
        return self.do_asym_encrypt(text, self.foreign_public_key)