from PIL import Image, ImageFilter, ImageEnhance
import matplotlib.pyplot as plt

# 1. Image Loading and Display
def load_and_display_image(image_path):
    image = Image.open(image_path)
    plt.imshow(image)
    plt.axis('off')  # Hide axes
    plt.show()
    return image

# 2. Image Manipulation

# Applying Gaussian Blur
def apply_gaussian_blur(image, radius=2):
    blurred_image = image.filter(ImageFilter.GaussianBlur(radius))
    return blurred_image

# Applying Edge Detection
def apply_edge_detection(image):
    edge_detected_image = image.filter(ImageFilter.FIND_EDGES)
    return edge_detected_image

# Changing Image Dimensions (Resizing)
def resize_image(image, width, height):
    resized_image = image.resize((width, height))
    return resized_image

# Cropping the Image
def crop_image(image, left, top, right, bottom):
    cropped_image = image.crop((left, top, right, bottom))
    return cropped_image

# Adjusting Brightness
def adjust_brightness(image, factor=1.5):
    enhancer = ImageEnhance.Brightness(image)
    brightened_image = enhancer.enhance(factor)
    return brightened_image

# Adjusting Contrast
def adjust_contrast(image, factor=1.5):
    enhancer = ImageEnhance.Contrast(image)
    contrasted_image = enhancer.enhance(factor)
    return contrasted_image

# Adjusting Saturation
def adjust_saturation(image, factor=1.5):
    enhancer = ImageEnhance.Color(image)
    saturated_image = enhancer.enhance(factor)
    return saturated_image

# Converting to Grayscale
def convert_to_grayscale(image):
    grayscale_image = image.convert("L")
    return grayscale_image

def display_all_images(images, titles):
    plt.figure(figsize=(15, 10))
    for i, (image, title) in enumerate(zip(images, titles)):
        plt.subplot(3, 3, i + 1)
        plt.imshow(image)
        plt.title(title)
        plt.axis('off')
    plt.tight_layout()
    plt.show()

# 3. Histogram Analysis
def display_histogram(image):
    plt.figure(figsize=(10, 5))
    color_channels = ('r', 'g', 'b')
    
    for i, color in enumerate(color_channels):
        histogram = image.histogram()[i * 256:(i + 1) * 256]
        plt.plot(histogram, color=color)
    
    plt.title('Color Histogram')
    plt.xlabel('Pixel value')
    plt.ylabel('Frequency')
    plt.show()

# Load and display the image
image_path = r"D:/5th Lab/Python/Lab 3/image.jpg"  
image = load_and_display_image(image_path)

# Apply Gaussian Blur
blurred_image = apply_gaussian_blur(image, radius=3)
plt.imshow(blurred_image)
plt.title('Gaussian Blurred Image')
plt.axis('off')

# Apply Edge Detection
edge_image = apply_edge_detection(image)
plt.imshow(edge_image)
plt.title('Edge Detected Image')
plt.axis('off')

# Resize Image
resized_image = resize_image(image, width=200, height=200)
plt.imshow(resized_image)
plt.title('Resized Image')
plt.axis('off')

# Crop Image
cropped_image = crop_image(image, left=50, top=50, right=250, bottom=250)
plt.imshow(cropped_image)
plt.title('Cropped Image')
plt.axis('off')

# Adjust Brightness
brightened_image = adjust_brightness(image, factor=1.8)
plt.imshow(brightened_image)
plt.title('Brightened Image')
plt.axis('off')

# Adjust Contrast
contrasted_image = adjust_contrast(image, factor=1.8)
plt.imshow(contrasted_image)
plt.title('Contrasted Image')
plt.axis('off')

# Adjust Saturation
saturated_image = adjust_saturation(image, factor=1.8)
plt.imshow(saturated_image)
plt.title('Saturated Image')
plt.axis('off')

# Convert to Grayscale
grayscale_image = convert_to_grayscale(image)
plt.imshow(grayscale_image, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')

images = [ image, blurred_image, edge_image, resized_image, cropped_image,brightened_image, contrasted_image, saturated_image, grayscale_image]
titles = ["Original Image", "Gaussian Blur", "Edge Detection", "Resized Image", "Cropped Image","Brightened Image", "Contrasted Image", "Saturated Image", "Grayscale Image"]
display_all_images(images, titles)

display_histogram(image)
