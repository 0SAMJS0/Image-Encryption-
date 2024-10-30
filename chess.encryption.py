from PIL import Image
import numpy as np

# Convert image to binary
def image_to_binary(image_path):
    image = Image.open(image_path).convert("L")  # Convert image to grayscale
    binary_data = ''.join(f'{pixel:08b}' for pixel in np.array(image).flatten())
    return binary_data

# Binary to chess moves (0 -> Pawn move, 1 -> Knight move)
def binary_to_chess_moves(binary_data):
    moves = []
    for bit in binary_data:
        if bit == '0':
            moves.append("Pawn move")  # Represent '0' as a pawn move
        else:
            moves.append("Knight move")  # Represent '1' as a knight move
    return moves

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

# Example of using the functions
def main():
    image_path = 'input_image.png'
    encrypted_output_path = 'decrypted_image.png'
    
    # Convert image to binary
    binary_data = image_to_binary(image_path)
    print("Binary data:", binary_data[:64], "...")  # Print the first 64 bits for verification
    
    # Encrypt: Binary to chess moves
    moves = binary_to_chess_moves(binary_data)
    print("Moves:", moves[:10], "...")  # Print the first 10 moves for verification
    
    # Decrypt: Chess moves back to binary
    decrypted_binary_data = chess_moves_to_binary(moves)
    
    # Verify decryption by comparing binary strings
    if binary_data == decrypted_binary_data:
        print("Decryption successful!")
    else:
        print("Decryption failed.")
    
    # Convert binary back to image
    image_shape = Image.open(image_path).size[::-1]  # Get the original image shape
    binary_to_image(decrypted_binary_data, image_shape, encrypted_output_path)
    print(f"Decrypted image saved as {encrypted_output_path}")

if __name__ == "__main__":
    main()
