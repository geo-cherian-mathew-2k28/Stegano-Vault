from PIL import Image
import numpy as np

class Steganography:
    def __init__(self):
        self.delimiter = "$$$" # Used to mark the end of the secret message

    def string_to_binary(self, data):
        """Convert any string to binary format."""
        # '08b' ensures each character is 8 bits
        return ''.join(format(ord(i), '08b') for i in data)

    def binary_to_string(self, binary_data):
        """Convert binary bits back to string."""
        all_bytes = [binary_data[i: i+8] for i in range(0, len(binary_data), 8)]
        decoded_data = ""
        for byte in all_bytes:
            decoded_data += chr(int(byte, 2))
            if decoded_data.endswith(self.delimiter):
                return decoded_data[:-len(self.delimiter)] # Remove the delimiter
        return decoded_data

    def encode(self, image_path, secret_message, output_path):
        """Encodes a message into the LSB of an image."""
        try:
            # Open image and convert to RGB (removes Alpha channel if present)
            image = Image.open(image_path).convert('RGB')
            pixels = np.array(image)
            
            # Add delimiter to message so we know when to stop reading
            secret_message += self.delimiter
            binary_message = self.string_to_binary(secret_message)
            data_len = len(binary_message)
            
            # Check if image is big enough
            total_pixels = pixels.size // 3 
            if data_len > total_pixels:
                raise ValueError(f"Message too long! Image can hold {total_pixels} bits, needed {data_len}.")

            print(f"[*] Encoding {data_len} bits into image...")

            # Flat iterator to loop through every value in the 3D array (Height, Width, RGB)
            iterator = np.nditer(pixels, flags=['multi_index'], op_flags=['readwrite'])
            
            idx = 0
            for value in iterator:
                if idx < data_len:
                    # Logic: Clear the last bit (bitwise AND with 254) 
                    # Then add our secret bit (bitwise OR)
                    bit = int(binary_message[idx])
                    value[...] = (value & 254) | bit
                    idx += 1
                else:
                    break

            # Save the new image
            encoded_image = Image.fromarray(pixels)
            encoded_image.save(output_path)
            print(f"[+] Success! Secret image saved as {output_path}")

        except Exception as e:
            print(f"[-] Error: {e}")

    def decode(self, image_path):
        """Decodes the LSB from an image to find the secret."""
        try:
            print("[*] Decoding image...")
            image = Image.open(image_path).convert('RGB')
            pixels = np.array(image)

            binary_data = ""
            for value in np.nditer(pixels):
                # Extract the last bit (bitwise AND with 1)
                binary_data += str(value & 1)

            # Convert binary to string
            message = self.binary_to_string(binary_data)
            return message

        except Exception as e:
            return f"[-] Error: {e}"

# --- CLI Menu ---
if __name__ == "__main__":
    tool = Steganography()
    
    print("=== Python LSB Steganography Tool ===")
    choice = input("1. Hide Message\n2. Reveal Message\nChoose: ")

    if choice == '1':
        img = input("Enter image name (e.g., cover.png): ")
        msg = input("Enter secret message: ")
        out = input("Enter output name (e.g., secret.png): ")
        tool.encode(img, msg, out)
    
    elif choice == '2':
        img = input("Enter image name (e.g., secret.png): ")
        result = tool.decode(img)
        print(f"\n[!] DECODED MESSAGE: \n{result}")
    else:
        print("Invalid choice.")