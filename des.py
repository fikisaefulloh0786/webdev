from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

# Fungsi untuk menghasilkan kunci DES acak
def generate_des_key():
    return get_random_bytes(8)  # DES menggunakan kunci 8 byte

# Fungsi untuk melakukan enkripsi
def encrypt_message(message, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_message = message + (8 - len(message) % 8) * " "  # Menyamakan panjang pesan dengan kelipatan 8
    encrypted_message = cipher.encrypt(padded_message.encode())
    return encrypted_message

# Fungsi untuk melakukan dekripsi
def decrypt_message(encrypted_message, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_message = cipher.decrypt(encrypted_message)
    return decrypted_message.rstrip(b" ").decode()

# Pesan yang ingin dienkripsi
message = input("Masukkan pesan: ")

# Generate kunci DES
des_key = generate_des_key()

# Melakukan enkripsi
encrypted_message = encrypt_message(message, des_key)
print("Pesan Terenkripsi:", encrypted_message.hex())

# Melakukan dekripsi
decrypted_message = decrypt_message(encrypted_message, des_key)
print("Pesan Terdekripsi:", decrypted_message)
