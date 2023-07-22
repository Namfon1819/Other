import cv2
import numpy as np

def divide_image(image, block_size, overlap):
    height, width = image.shape[:2]  # Get image dimensions
    channels = image.shape[2] if len(image.shape) == 3 else 1  # Check number of channels
    stride = block_size - overlap
    
    # Calculate the number of blocks in each dimension
    num_blocks_h = (height - overlap) // stride
    num_blocks_w = (width - overlap) // stride
    
    blocks = []
    
    for i in range(num_blocks_h):
        for j in range(num_blocks_w):
            start_h = i * stride
            end_h = start_h + block_size
            
            start_w = j * stride
            end_w = start_w + block_size
            
            block = image[start_h:end_h, start_w:end_w]
            blocks.append(block)
    
    return blocks

def reconstruct_image(blocks, block_size, overlap):
    stride = block_size - overlap
    num_blocks_h = len(blocks) // num_blocks_w
    
    full_height = num_blocks_h * stride + block_size
    full_width = num_blocks_w * stride + block_size
    
    if channels == 1:
        reconstructed_image = np.zeros((full_height, full_width), dtype=np.uint8)
    else:
        reconstructed_image = np.zeros((full_height, full_width, channels), dtype=np.uint8)
    
    block_index = 0
    
    for i in range(num_blocks_h):
        for j in range(num_blocks_w):
            start_h = i * stride
            end_h = start_h + block_size
            
            start_w = j * stride
            end_w = start_w + block_size
            
            reconstructed_image[start_h:end_h, start_w:end_w] = blocks[block_index]
            block_index += 1
    
    return reconstructed_image

# Load the image
image = cv2.imread(r"C:\teacher\assignment1\image.jpg", cv2.IMREAD_GRAYSCALE)

# Check if the image is grayscale and convert it to color if needed
if len(image.shape) == 2:
    image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

# Define block size and overlap
block_size = 100  # Size of each block (e.g., 100x100 pixels)
overlap = 25     # Overlap between blocks (e.g., 25 pixels)

# Divide the image into overlapping blocks
blocks = divide_image(image, block_size, overlap)

# Reconstruct the image from the blocks
reconstructed_image = reconstruct_image(blocks, block_size, overlap)

# Draw vertical lines between blocks
for i in range(0, reconstructed_image.shape[1], block_size):
    cv2.line(reconstructed_image, (i, 0), (i, reconstructed_image.shape[0]), (0, 0, 255), 2)

# Draw horizontal lines between blocks
for j in range(0, reconstructed_image.shape[0], block_size):
    cv2.line(reconstructed_image, (0, j), (reconstructed_image.shape[1], j), (0, 0, 255), 2)

# Display the original and reconstructed images side by side
cv2.imshow('Original Image', image)
cv2.imshow('Reconstructed Image', reconstructed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

