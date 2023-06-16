from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import hashlib

def encrypt_image(image_path, key):
    # Resmi okuma işlemi Yapılır
    with open(image_path, 'rb') as file:
        image_data = file.read()

    # Generate a 256-bit key using SHA-256 hash function
    hashed_key = hashlib.sha256(key.encode()).digest()

    # Create an AES cipher object with the key
    cipher = AES.new(hashed_key, AES.MODE_ECB)

    # Pad the image data to match the AES block size
    padded_image_data = pad(image_data, AES.block_size)

    # Encrypt the padded image data
    encrypted_data = cipher.encrypt(padded_image_data)

    # Save the encrypted data to a new file
    encrypted_image_path = image_path
    with open(encrypted_image_path, 'wb') as file:
        file.write(encrypted_data)

    return encrypted_image_path

# Usage example
image_path = 'C:/Users/ahmet/Downloads/sinifDersler/bitirmePro/Konum.png'
encryption_key = 'myencryptionkey'
encrypted_image = encrypt_image(image_path, encryption_key)
print("Image encrypted successfully:", encrypted_image)

from Crypto.Util.Padding import pad

data = b'Secret message'
block_size = 16  # Block size in bytes

padded_data = pad(data, block_size)

print(padded_data)