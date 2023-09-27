from cryptography.fernet import Fernet
import rsa
from rsa import PrivateKey, PublicKey
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


class Encryption:

    # Генерация пары ключей
    def key_pair_gen(self):
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=1024,
        )
        # Serialize the private key
        private_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )
        # Serialize the public key
        public_key = private_key.public_key()
        public_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        print(private_pem, public_pem)
        return private_pem, public_pem
    
    def __init__(self):
        self.key = b'LYCLog-4JekRS3ssP4OVNT104eIRwiEDBMMrdjv4mg0='
        self.fernet_key = Fernet(self.key)
        self.public_key_another = None
        self.key_pair_gen()

    # Симметричное шифрование - дешифрование
    def symm_encrypt(self, message: bytes) -> bytes:
        return self.fernet_key.encrypt(message)
    def symm_decrypt(self, ciphertext: bytes) -> bytes:
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
        self.public_key_another = rsa.PublicKey.load_pkcs1(public_key)

    # Расшифровка полученного сообщения
    def do_asym_decrypt_of_foreign_message(self, ciphertext: bytes) -> bytes:
        return self.do_asym_decrypt(ciphertext, self.private_key)
        return rsa.decrypt()
    
    # Шифрование сообщения
    def do_asym_encrypt_of_message(self, text: bytes) -> bytes:
        return self.do_asym_encrypt(text, self.public_key_another)
    
enc = Encryption()