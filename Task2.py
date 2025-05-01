from PIL import Image
import os

def encrypt_decrypt_image(input_path, output_path, key):
    try:
        img = Image.open(input_path)
        img = img.convert('RGB')  # Ensure image is in RGB mode
        pixels = img.load()

        width, height = img.size
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                # XOR operation with key
                pixels[x, y] = (r ^ key, g ^ key, b ^ key)

        img.save(output_path)
        print(f"Operation successful. Saved as: {output_path}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("=== Image Encryption & Decryption Tool ===")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()
    input_path = input("Enter input image path: ").strip()
    output_path = input("Enter output image path: ").strip()
    try:
        key = int(input("Enter numeric key (0-255): ").strip())
        if not (0 <= key <= 255):
            raise ValueError("Key must be between 0 and 255.")
    except ValueError as ve:
        print(f"Invalid key: {ve}")
        return

    if not os.path.exists(input_path):
        print("Input file does not exist.")
        return

    encrypt_decrypt_image(input_path, output_path, key)

if __name__ == "__main__":
    main()
