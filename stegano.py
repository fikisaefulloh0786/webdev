from PIL import Image

# Fungsi untuk menyembunyikan pesan dalam gambar
def hide_message_in_image(input_image_path, output_image_path, message):
    # Buka gambar
    image = Image.open(input_image_path)

    # Konversi pesan menjadi binary
    binary_message = ''.join(format(ord(char), '08b') for char in message)

    # Pastikan pesan sesuai dengan ukuran gambar
    if len(binary_message) > image.width * image.height:
        raise ValueError("Pesan terlalu besar untuk gambar ini")

    # Iterasi melalui piksel gambar dan pesan, menyembunyikan pesan dalam piksel LSB
    message_index = 0
    for x in range(image.width):
        for y in range(image.height):
            pixel = list(image.getpixel((x, y)))
            for color_channel in range(3):  # R, G, B
                if message_index < len(binary_message):
                    pixel[color_channel] = pixel[color_channel] & ~1 | int(binary_message[message_index])
                    message_index += 1
            image.putpixel((x, y), tuple(pixel))

    # Simpan gambar yang telah dimodifikasi
    image.save(output_image_path)

# Fungsi untuk mengekstrak pesan yang tersembunyi dalam gambar
def extract_message_from_image(image_path):
    # Buka gambar
    image = Image.open(image_path)
    binary_message = ''

    # Iterasi melalui piksel gambar untuk mengekstrak pesan dari LSB
    for x in range(image.width):
        for y in range(image.height):
            pixel = list(image.getpixel((x, y)))
            for color_channel in range(3):  # R, G, B
                binary_message += str(pixel[color_channel] & 1)

    # Konversi binary menjadi pesan teks
    message = ''.join(chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message), 8))

    return message

# Pesan yang akan disembunyikan dalam gambar
message_to_hide = "Ini adalah pesan rahasia yang akan disembunyikan dalam gambar."

# Menyembunyikan pesan dalam gambar
hide_message_in_image('logo.jpg', 'output_image.png', message_to_hide)

# Mengekstrak pesan dari gambar yang telah disembunyikan
extracted_message = extract_message_from_image('output_image.png')
print("Pesan Tersembunyi yang Diekstrak:", extracted_message)
