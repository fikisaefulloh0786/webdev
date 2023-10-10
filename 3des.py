from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes

# Fungsi untuk menghasilkan kunci 3DES acak
def generate_des3_key():
    return get_random_bytes(24)  # 3DES menggunakan kunci 24 byte

# Fungsi untuk melakukan enkripsi
def encrypt_message(message, key):
    cipher = DES3.new(key, DES3.MODE_ECB)
    padded_message = message + (8 - len(message) % 8) * " "  # Menyamakan panjang pesan dengan kelipatan 8
    encrypted_message = cipher.encrypt(padded_message.encode())
    return encrypted_message

# Fungsi untuk melakukan dekripsi
def decrypt_message(encrypted_message, key):
    cipher = DES3.new(key, DES3.MODE_ECB)
    decrypted_message = cipher.decrypt(encrypted_message)
    return decrypted_message.rstrip(b" ").decode()

# Pesan yang ingin dienkripsi
message = input("Masukkan pesan: ")

# Generate kunci 3DES
des3_key = generate_des3_key()

# Melakukan enkripsi
encrypted_message = encrypt_message(message, des3_key)
print("Pesan Terenkripsi:", encrypted_message.hex())

# Melakukan dekripsi
decrypted_message = decrypt_message(encrypted_message, des3_key)
print("Pesan Terdekripsi:", decrypted_message)
