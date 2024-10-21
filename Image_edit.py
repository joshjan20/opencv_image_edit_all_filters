import cv2
import numpy as np

def apply_filter(image, filter_type):
    """Apply a selected filter to the image."""
    if filter_type == 'blur':
        return cv2.GaussianBlur(image, (15, 15), 0)
    elif filter_type == 'sharpen':
        kernel = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]])
        return cv2.filter2D(image, -1, kernel)
    elif filter_type == 'edge_detection':
        return cv2.Canny(image, 100, 200)
    elif filter_type == 'emboss':
        kernel = np.array([[2, 0, 0],
                           [0, -1, 0],
                           [0, 0, -1]])
        return cv2.filter2D(image, -1, kernel)
    else:
        print("Filter type not recognized.")
        return image

def enhance_contrast(image):
    """Improve image quality by enhancing contrast using CLAHE."""
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    cl = clahe.apply(l)
    limg = cv2.merge((cl, a, b))
    return cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)

def increase_brightness(image, value=30):
    """Increase the brightness of the image."""
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    v = cv2.add(v, value)
    v[v > 255] = 255
    v[v < 0] = 0
    final_hsv = cv2.merge((h, s, v))
    return cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)

def adjust_saturation(image, saturation_scale=1.5):
    """Adjust the saturation of the image."""
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    s = cv2.multiply(s, saturation_scale)
    s[s > 255] = 255
    final_hsv = cv2.merge((h, s, v))
    return cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)

def convert_to_grayscale(image):
    """Convert the image to grayscale."""
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def apply_sepia(image):
    """Apply sepia effect to the image."""
    sepia_filter = np.array([[0.272, 0.534, 0.131],
                             [0.349, 0.686, 0.168],
                             [0.393, 0.769, 0.189]])
    sepia_image = cv2.transform(image, sepia_filter)
    sepia_image = np.clip(sepia_image, 0, 255)
    return sepia_image.astype(np.uint8)

def histogram_equalization(image):
    """Apply histogram equalization to enhance the image contrast."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    equalized_img = cv2.equalizeHist(gray)
    return cv2.cvtColor(equalized_img, cv2.COLOR_GRAY2BGR)

def add_text(image, text, position=(50, 50), font_scale=1, color=(0, 255, 0), thickness=2):
    """Add text to the image."""
    return cv2.putText(image, text, position, cv2.FONT_HERSHEY_SIMPLEX, font_scale, color, thickness)

def main():
    # Load image
    image_path = 'assets/mountain.png'
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Unable to load image {image_path}")
        return

    while True:
        # Display the original image
        cv2.imshow('Original Image', img)

        print("\nChoose an operation:")
        print("1. Apply Filter (blur, sharpen, edge_detection, emboss)")
        print("2. Enhance Contrast")
        print("3. Increase Brightness")
        print("4. Adjust Saturation")
        print("5. Convert to Grayscale")
        print("6. Apply Sepia Effect")
        print("7. Histogram Equalization")
        print("8. Add Text/Watermark")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            filter_type = input("Enter filter type (blur, sharpen, edge_detection, emboss): ")
            filtered_img = apply_filter(img, filter_type)
            cv2.imshow(f'{filter_type.capitalize()} Filter', filtered_img)

        elif choice == '2':
            enhanced_img = enhance_contrast(img)
            cv2.imshow('Enhanced Contrast', enhanced_img)

        elif choice == '3':
            brightness_value = int(input("Enter brightness increase value (default 30): "))
            bright_img = increase_brightness(img, brightness_value)
            cv2.imshow('Increased Brightness', bright_img)

        elif choice == '4':
            saturation_scale = float(input("Enter saturation scale (default 1.5): "))
            saturated_img = adjust_saturation(img, saturation_scale)
            cv2.imshow('Adjusted Saturation', saturated_img)

        elif choice == '5':
            grayscale_img = convert_to_grayscale(img)
            cv2.imshow('Grayscale Image', grayscale_img)

        elif choice == '6':
            sepia_img = apply_sepia(img)
            cv2.imshow('Sepia Effect', sepia_img)

        elif choice == '7':
            equalized_img = histogram_equalization(img)
            cv2.imshow('Histogram Equalization', equalized_img)

        elif choice == '8':
            text = input("Enter the text to add: ")
            position = tuple(map(int, input("Enter text position as x, y: ").split(',')))
            watermarked_img = add_text(img, text, position)
            cv2.imshow('Text/Watermark Added', watermarked_img)

        elif choice == '9':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

        if cv2.waitKey(1) == ord('q'):
            break

    # Cleanup
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
