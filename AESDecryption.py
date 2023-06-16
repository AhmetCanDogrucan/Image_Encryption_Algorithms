from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import hashlib

def decrypt_image(encrypted_image_path, key):
    # Read the encrypted image file
    with open(encrypted_image_path, 'rb') as file:
        encrypted_data = file.read()

    # Generate a 256-bit key using SHA-256 hash function
    hashed_key = hashlib.sha256(key.encode()).digest()

    # Create an AES cipher object with the key
    cipher = AES.new(hashed_key, AES.MODE_ECB)

    # Decrypt the encrypted data
    decrypted_data = cipher.decrypt(encrypted_data)

    # Unpad the decrypted data
    unpadded_data = unpad(decrypted_data, AES.block_size)

    # Save the decrypted data to a new file
    decrypted_image_path = encrypted_image_path.replace(".encrypted","")
    with open(decrypted_image_path, 'wb') as file:
        file.write(unpadded_data)

    return decrypted_image_path

# Usage example
encrypted_image_path = 'C:/Users/ahmet/Downloads/sinifDersler/bitirmePro/Cameraman.bmp.encrypted'
decryption_key = 'myencryptionkey'
decrypted_image = decrypt_image(encrypted_image_path, decryption_key)
print("Image decrypted successfully:", decrypted_image)