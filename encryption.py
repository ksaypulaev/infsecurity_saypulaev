from cryptography.fernet import Fernet
import rsa
from rsa import PrivateKey, PublicKey
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import os


class Encryption:

    def __init__(self):
        #self.key = b'LYCLog-4JekRS3ssP4OVNT104eIRwiEDBMMrdjv4mg0='
        self.pathh = "/Users/ksaypulaev/Desktop/Инф безопасность/КДЗ/keys/key.pem"
    
    # Генерация ключа и запись в файл
    def key_gen(self):
        if os.path.exists("/Users/ksaypulaev/Desktop/Инф безопасность/КДЗ/keys"):
            if os.path.isfile(self.pathh):
                pass
            else:
                key_generated = Fernet.generate_key()
                #print(key_generated)
                with open(self.pathh, "w") as file:
                    file.write(key_generated.decode())
    
    # Чтение ключа из файла
    def key_read(self):
        with open(self.pathh, "r") as file:
            text = file.read().encode('utf-8')
        fernet_key = Fernet(text)
        #print(text)
        return fernet_key

    # Симметричное шифрование - дешифрование
    def symm_encrypt(self, message: bytes) -> bytes:
        return self.key_read().encrypt(message)
    def symm_decrypt(self, ciphertext: bytes) -> bytes:
        return self.key_read().decrypt(ciphertext)
    
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
        #print(private_pem, public_pem)
        return private_pem, public_pem
    
#enc = Encryption()
#enc.key_gen()
#enc.key_read()
#enc.symm_encrypt(b'Hello')