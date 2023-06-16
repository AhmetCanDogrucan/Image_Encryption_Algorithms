import numpy as np
from PIL import Image

def tent_map(x, a):
    if x < a:
        return x / a
    else:
        return (1 - x) / (1 - a)

def encrypt_image(image_path, output_path):
    #resim açılıp gri tona çevrilmesi
    image = Image.open(image_path).convert('L')
    #pixel degerlerinin alınması
    pixels = np.array(image)
    height, width = pixels.shape
    #başlangıc parametrelerinin verilmesi
    a = 0.7  # Tent map parameter
    x = 0.2  # Initial value
    #iterasyon sayısının belirlenmesi
    n_iterations = height * width  # Number of iterations
    #sıfırlardan oluşan bir goruntunun oluşturulması
    encrypted_pixels = np.zeros((height, width), dtype=np.uint8)

    for i in range(n_iterations):
        #değerlerin şifreleme algoritmasına gönderilmesi
        x = tent_map(x, a)
        row = i // width
        col = i % width
        #şifreleme denkleminden gelen degerin piksel değerleriyle XOR işleminn uygulanması
        encrypted_pixels[row, col] = np.uint8(pixels[row, col] ^ int(x * 255))

    encrypted_image = Image.fromarray(encrypted_pixels)
    encrypted_image.save(output_path)
    print("Image encrypted successfully.")

def decrypt_image(encrypted_image_path, output_path):
    encrypted_image = Image.open(encrypted_image_path).convert('L')
    encrypted_pixels = np.array(encrypted_image)
    height, width = encrypted_pixels.shape

    a = 0.7  # Tent map parameter
    x = 0.2  # Initial value
    n_iterations = height * width  # Number of iterations

    decrypted_pixels = np.zeros((height, width), dtype=np.uint8)

    for i in range(n_iterations):
        x = tent_map(x, a)
        row = i // width
        col = i % width
        decrypted_pixels[row, col] = np.uint8(encrypted_pixels[row, col] ^ int(x * 255))

    decrypted_image = Image.fromarray(decrypted_pixels)
    decrypted_image.save(output_path)
    print("Image decrypted successfully.")

if __name__ == '__main__':
    # Specify the image file paths
    input_image_path = 'C:/Users/ahmet/Downloads/sinifDersler/bitirmePro/Pepper.bmp'
    encrypted_image_path = 'C:/Users/ahmet/Downloads/sinifDersler/bitirmePro/TentEncPepper.bmp'
    decrypted_image_path = 'C:/Users/ahmet/Downloads/sinifDersler/bitirmePro/DePepper.bmp'

    # Encrypt the image
    encrypt_image(input_image_path, encrypted_image_path)

    # Decrypt the image
    decrypt_image(encrypted_image_path, decrypted_image_path)