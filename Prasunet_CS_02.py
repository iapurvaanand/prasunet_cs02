try:
        image = Image.open(image_path)
        image = image.convert('RGB')  
        pixels = np.array(image)
        
        # key range
        key = key % 256
        
        # random calculation 
        encrypted_pixels = (pixels + key) % 256
        
        # encryption
        encrypted_image = Image.fromarray(encrypted_pixels.astype('uint8'))
        encrypted_image.save(output_path)
        print(f"Encrypted image saved to {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def decrypt_image(encrypted_image_path, output_path, key):
    try:
        encrypted_image = Image.open(encrypted_image_path)
        encrypted_image = encrypted_image.convert('RGB')  # Ensure image is in RGB mode
        encrypted_pixels = np.array(encrypted_image)
        
        # Ensure the key is within the range [0, 255]
        key = key % 256
        
        # Reverse the mathematical operation to decrypt
        decrypted_pixels = (encrypted_pixels - key) % 256
        
        # Create a new decrypted image
        decrypted_image = Image.fromarray(decrypted_pixels.astype('uint8'))
        decrypted_image.save(output_path)
        print(f"Decrypted image saved to {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    while True:
        choice = input("Enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit: ").lower()
        if choice == 'q':
            break
        if choice not in ['e', 'd']:
            print("Invalid choice. Please enter 'e', 'd', or 'q'.")
            continue
        
        image_path = input("Enter the path of the image: ")
        output_path = input("Enter the path to save the output image: ")
        
        try:
            key = int(input("Enter the encryption/decryption key (integer): "))
        except ValueError:
            print("Invalid key. Please enter an integer.")
            continue
        
        if choice == 'e':
            encrypt_image(image_path, output_path, key)
        elif choice == 'd':
            decrypt_image(image_path, output_path, key)

if _name_ == "_main_":
    main()