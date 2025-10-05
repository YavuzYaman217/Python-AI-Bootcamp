# Import NumPy library for efficient numerical operations and array manipulation
import numpy as np

# Define the dimensions of our simulated image
img_height = 100  # Image height in pixels
img_width = 150   # Image width in pixels

# Create a random RGB image with pixel values ranging from 0 to 255
# Shape: (100, 150, 3) where 3 represents RGB color channels (Red, Green, Blue)
# dtype=np.uint8 ensures pixel values are 8-bit unsigned integers (0-255 range)
image_data = np.random.randint(0, 256, (img_height, img_width, 3), dtype=np.uint8)

def to_grayscale(pixel: np.ndarray) -> np.uint8:
    """
    Convert a pixel from RGB to grayscale using the luminosity method.
    
    This method accounts for human eye sensitivity to different colors:
    - Human eyes are most sensitive to green (58.7% weight)
    - Moderately sensitive to red (29.9% weight)
    - Least sensitive to blue (11.4% weight)
    
    Formula: Y = 0.299*R + 0.587*G + 0.114*B
    
    Args:
        pixel (np.ndarray): RGB pixel array with values [R, G, B]
    
    Returns:
        np.uint8: Grayscale intensity value (0-255)
    """
    # Calculate weighted average of RGB channels and convert to 8-bit integer
    return np.uint8(0.299 * pixel[0] + 0.587 * pixel[1] + 0.114 * pixel[2])



# Convert RGB image to grayscale by applying the to_grayscale function to each pixel
# np.apply_along_axis applies the function along axis 2 (the color channel axis)
# This processes each RGB pixel [R, G, B] and converts it to a single grayscale value
grayscale_image = np.apply_along_axis(to_grayscale, 2, image_data)

# Create a negative (inverted) image by subtracting each pixel value from 255
# This inverts the intensity: dark pixels become bright and bright pixels become dark
# Example: pixel value 200 becomes 55, pixel value 50 becomes 205
negative_image = 255 - grayscale_image

# Count the number of pixels that are brighter than the average brightness
# flatten() converts the 2D image array into a 1D array for easier iteration
# We compare each pixel to the mean grayscale value to determine if it's "bright"
bright_pixels = sum(1 for pixel in grayscale_image.flatten() if pixel > np.mean(grayscale_image))


# Display the results of our image processing operations
# Original image has 3 dimensions: (height, width, color_channels)
print(f"Original Image Shape: {image_data.shape}")

# Grayscale image has 2 dimensions: (height, width) - no color channels
print(f"Grayscale Image Shape: {grayscale_image.shape}")

# Negative image maintains the same shape as the grayscale image
print(f"Negative Image Shape: {negative_image.shape}")

# Show how many pixels are brighter than the average brightness level
print(f"Bright Pixels Count: {bright_pixels}")