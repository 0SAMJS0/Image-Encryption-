from PIL import Image
import numpy as np

# Chess moves to binary
def chess_moves_to_binary(moves):
    binary_data = ''
    for move in moves:
        if move == "Pawn move":
            binary_data += '0'
        elif move == "Knight move":
            binary_data += '1'
    return binary_data

# Convert binary back to image
def binary_to_image(binary_data, image_shape, output_path):
    pixel_data = [int(binary_data[i:i+8], 2) for i in range(0, len(binary_data), 8)]
    pixel_array = np.array(pixel_data, dtype=np.uint8).reshape(image_shape)
    image = Image.fromarray(pixel_array, 'L')
    image.save(output_path)

# Example of decryption process
def decrypt_chess_moves_to_image(moves, original_image_shape, output_path):
    # Convert moves back to binary
    binary_data = chess_moves_to_binary(moves)
    
    # Convert binary data back to image
    binary_to_image(binary_data, original_image_shape, output_path)
    print(f"Decrypted image saved as {output_path}")

# Usage example
def main():
    # Example of moves sequence to be decrypted
    moves = ["Pawn move", "Knight move", "Pawn move", "Knight move", "Knight move", "Pawn move"]  # Replace with actual moves sequence

    # Original image dimensions
    original_image_shape = (256, 256)  # Example shape; replace with actual image shape

    # Path to save the decrypted image
    output_path = 'decrypted_image.png'

    # Decrypt moves to image
    decrypt_chess_moves_to_image(moves, original_image_shape, output_path)

if __name__ == "__main__":
    main()
