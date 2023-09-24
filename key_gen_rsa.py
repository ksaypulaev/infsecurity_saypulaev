from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


private_path = '/Users/ksaypulaev/Desktop/Инф безопасность/КДЗ/keys2/private_key.pem'
public_path = '/Users/ksaypulaev/Desktop/Инф безопасность/КДЗ/keys2/public_key.pem'

# Generate a key pair
private_key = rsa.generate_private_key(public_exponent=65537,key_size=2048)

# Serialize the private key to a file (store it securely)
with open(private_path, "wb") as private_key_file:
    private_key_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    private_key_file.write(private_key_pem)

# Get the public key
public_key = private_key.public_key()

# Serialize the public key to a file (this can be shared)
with open(public_path, "wb") as public_key_file:
    public_key_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    public_key_file.write(public_key_pem)

print(private_key_pem.decode())
print(public_key_pem.decode())