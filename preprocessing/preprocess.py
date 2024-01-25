import cv2
from PIL import Image
import numpy as np

def Noise_Reduction(image_path):
    img = cv2.imread(image_path)

    # Apply Gaussian Blur, low pass filter, reduce high frequency noise
    # Reference: https://www.w3.org/Talks/2012/0125-HTML-Tehran/Gaussian.xhtml
    # Why: reduce image noise and detail
    # How: Gaussian kernal, convoluted thoughout the image, bell curve in 2d
    Gb_blur = cv2.GaussianBlur(img, ksize=(5,7), sigmaX=10, sigmaY=10)

    # Apply Median Filter
    # Why: further eliminate salt-and-pepper noise (random, isolated extreme high/low noise), which Gassian Blur is unable to do
    # How: find the median of a kernal, apply median value to all pixel in a kernal
    MF = cv2.medianBlur(Gb_blur, ksize=5)

    # Apply Bilateral Filter
    # Why: smooth the image while preserving edges, maintaining the sharpness of text edges
    # How: taken into account in both spatial closeness and intensity similarity of pixels
    BF = cv2.bilateralFilter(MF)


    # Apply Thresholding
    # Why: Thresholding helps in distinguishing between foreground (text) and background.
    # How: Convert the image into a binary format

    # Morphological Operations
    # erosion and dilation to clean up the binary image. This can help remove small noise and connect broken parts of characters.

    # Contrast Limited Adaptive Histogram Equalization (CLAHE)

    # Anisotropic Diffusion

    # Wavelet Transform

    # Image Pyramids

def Binarization():
    #   Convert the image to binary format (black and white) for better character separation.
      pass

def text_localization():
    # Identify and extract regions containing text using techniques like contour detection.
    pass




image = cv2.imread("../data/chapter-1_page22.jpg")

# ksize = kernal size, larger ksize = more blur, sigma = wider and smoother blur
blur = cv2.GaussianBlur(image, ksize=(5,7), sigmaX=10, sigmaY=10)

MF = cv2.medianBlur(blur, ksize=5)

BF = cv2.bilateralFilter(MF, d=5, sigmaColor=1, sigmaSpace=2)


with open("image.jpg", "wb") as file:
        file.write(blur)

final = Image.fromarray(blur.astype('uint8'))

final.save("output_image.jpg")

cv2.imshow("", BF)
cv2.waitKey(0)


# Morphological Operations:

# Use morphological operations like erosion and dilation to clean up the binary image. This can help remove small noise and connect broken parts of characters.
# Contrast Limited Adaptive Histogram Equalization (CLAHE):

# Enhance local contrast using CLAHE to improve the visibility of text. This can be particularly useful if there are variations in lighting across the image.
# Anisotropic Diffusion:

# Apply anisotropic diffusion to selectively smooth the image while preserving edges. This can help in further reducing noise without compromising important details.
# Wavelet Transform:

# Use wavelet transform for multiresolution analysis. Apply thresholding or filtering to different frequency components to address noise at various scales.
# Image Pyramids:

# Construct image pyramids and process the image at different scales. This can help in smoothing out noise at higher resolutions while preserving essential details at lower resolutions.