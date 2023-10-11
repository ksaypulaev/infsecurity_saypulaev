# Шифрование сообщений

[Ссылка на профиль](https://github.com/ksaypulaev "https://github.com/ksaypulaev")\
[https://github.com/ksaypulaev/infsecurity_saypulaev](https://github.com/ksaypulaev/infsecurity_saypulaev "https://github.com/ksaypulaev/infsecurity_saypulaev")
### Table of contents:
1. Server.py - сервер.
2. Client.py - клиент, передающий и получаюший сообщения.
3. Encryption.py - класс генегирует ключ, записывает его в файл и проверяет его наличие в файле. Есть метод шифрования и дешифрования сообщения. Симметричное шифрование и генерация ключа реализованы библиотекой Fernet, которая использует алгоритм AES со 128-битными блоками и 256-битным ключом.