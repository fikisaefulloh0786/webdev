from Crypto.Cipher import Blowfish
from Crypto.Random import get_random_bytes
import base64

# Fungsi untuk menghasilkan kunci Blowfish acak
def generate_blowfish_key():
    return get_random_bytes(16)  # Blowfish menggunakan kunci 16 byte

# Fungsi untuk melakukan enkripsi
def encrypt_message(message, key):
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    padded_message = message + (8 - len(message) % 8) * " "  # Menyamakan panjang pesan dengan kelipatan 8
    encrypted_message = cipher.encrypt(padded_message.encode())
    return base64.b64encode(encrypted_message).decode()

# Fungsi untuk melakukan dekripsi
def decrypt_message(encrypted_message, key):
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    encrypted_message = base64.b64decode(encrypted_message)
    decrypted_message = cipher.decrypt(encrypted_message)
    return decrypted_message.rstrip(b" ").decode()

# Pesan yang ingin dienkripsi
message = input("Masukkan pesan: ")

# Generate kunci Blowfish
blowfish_key = generate_blowfish_key()

# Melakukan enkripsi
encrypted_message = encrypt_message(message, blowfish_key)
print("Pesan Terenkripsi:", encrypted_message)

# Melakukan dekripsi
decrypted_message = decrypt_message(encrypted_message, blowfish_key)
print("Pesan Terdekripsi:", decrypted_message)
