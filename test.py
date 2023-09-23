from cryptography.fernet import Fernet


message = 'Hello World!'
message = message.encode('utf-8')

key = Fernet.generate_key()

# Синхронное шифрование сообщения
key_fernet_object = Fernet(key)
encrypted_message = Fernet.encrypt(key_fernet_object, message)
print(encrypted_message)

# Синхронное дешифрование сообщения
decrypted_message = Fernet.decrypt(key_fernet_object, encrypted_message)
print(decrypted_message)