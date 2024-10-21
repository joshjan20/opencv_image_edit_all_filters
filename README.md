# Image Editing with OpenCV and Python

This Python script demonstrates various image editing and enhancement functionalities using **OpenCV** and **NumPy** libraries. The script allows you to apply filters, adjust brightness, contrast, saturation, and even add text or watermarks to an image. You can also convert the image to grayscale, apply a sepia effect, and more.

## Features

1. **Apply Filters**: Choose from filters like blur, sharpen, edge detection, and emboss.
2. **Enhance Contrast**: Improve the contrast of your images using CLAHE (Contrast Limited Adaptive Histogram Equalization).
3. **Increase Brightness**: Boost the brightness of the image.
4. **Adjust Saturation**: Modify the color intensity (saturation) of the image.
5. **Convert to Grayscale**: Convert a color image to grayscale.
6. **Apply Sepia Effect**: Give your images a vintage sepia effect.
7. **Histogram Equalization**: Enhance contrast by redistributing pixel intensities in the image.
8. **Add Text/Watermark**: Overlay custom text or watermark onto the image.

## Prerequisites

Ensure you have **Python 3.x** installed. You will also need the following libraries:

- OpenCV
- NumPy

To install the required packages, run:

```bash
pip install opencv-python numpy
```

## Getting Started

### 1. Clone the Repository

Clone or download the repository to your local machine.

```bash
git clone https://github.com/your-repo/image_editing.git
```

### 2. Add an Image

Place an image that you want to edit inside the `assets` directory. By default, the script looks for an image named `sample.jpg`. You can modify the image path in the code if necessary.

### 3. Run the Script

To run the image editing script, execute the following command:

```bash
python Image_edit.py
```

### 4. Follow the Prompts

The script will display the original image and prompt you to select from a list of operations:

1. **Apply Filter**: Choose a filter (blur, sharpen, edge detection, emboss).
2. **Enhance Contrast**: Use CLAHE to improve the contrast of the image.
3. **Increase Brightness**: Provide a value to increase the brightness.
4. **Adjust Saturation**: Provide a scale factor to adjust the saturation.
5. **Convert to Grayscale**: Convert the image to grayscale.
6. **Apply Sepia Effect**: Apply a sepia filter to the image.
7. **Histogram Equalization**: Enhance contrast using histogram equalization.
8. **Add Text/Watermark**: Enter custom text and its position to overlay it on the image.
9. **Exit**: Quit the program.

After performing each operation, the modified image will be displayed in a separate window. Press `q` or close the window to exit the current operation.

### Example:

Here is an example of running the script and choosing an operation:

```bash
Choose an operation:
1. Apply Filter (blur, sharpen, edge_detection, emboss)
2. Enhance Contrast
3. Increase Brightness
4. Adjust Saturation
5. Convert to Grayscale
6. Apply Sepia Effect
7. Histogram Equalization
8. Add Text/Watermark
9. Exit
```

## Code Overview

Here’s a quick look at the main components of the script:

- **apply_filter(image, filter_type)**: Applies filters like blur, sharpen, edge detection, and emboss.
- **enhance_contrast(image)**: Uses CLAHE to enhance contrast.
- **increase_brightness(image, value)**: Increases the brightness by adding a value to the pixel intensities.
- **adjust_saturation(image, saturation_scale)**: Adjusts saturation by scaling the saturation channel of the HSV image.
- **convert_to_grayscale(image)**: Converts the image to grayscale.
- **apply_sepia(image)**: Applies a sepia effect to give the image a vintage look.
- **histogram_equalization(image)**: Applies histogram equalization to enhance contrast.
- **add_text(image, text, position)**: Adds a text or watermark to the image at the specified position.

## Usage

1. Run the script with an image, and choose an operation from the list.
2. Apply the desired effect, and view the result.
3. Close the window or press `q` to exit and move to the next operation.

### Exiting the Program:

You can exit the program at any time by pressing `q` in any displayed window or selecting `Exit` from the main menu.

## Example Operations:

Here are a few examples of what you can do:

- **Blur the image**: Smooth the image by applying Gaussian blur.
- **Sharpen the image**: Enhance the sharpness of edges.
- **Edge Detection**: Detect edges using the Canny edge detection method.
- **Increase Brightness**: Brighten the image to reveal hidden details.
- **Sepia Effect**: Add a warm, brownish tint to give the image a retro feel.
- **Add Watermark**: Overlay custom text like a watermark on the image.

## Screenshots

### Original Image
<img src="assets/sample.jpg" alt="Original Image" width="300">

### After Applying Sepia Effect
<img src="assets/sample_sepia.jpg" alt="Sepia Image" width="300">

### Watermarked Image
<img src="assets/sample_watermarked.jpg" alt="Watermarked Image" width="300">

## Conclusion

This script is a simple yet powerful tool for image editing using OpenCV in Python. With the ability to apply filters, adjust image properties like brightness and contrast, and even add watermarks, it serves as a flexible solution for quick image processing tasks.

Feel free to explore and modify the script to suit your needs!

---