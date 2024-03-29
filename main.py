import pytesseract
import argparse
from easyocr import Reader
from PIL import Image


# page segmentation mode
"""
  0    Orientation and script detection (OSD) only.
  1    Automatic page segmentation with OSD.
  2    Automatic page segmentation, but no OSD, or OCR.
  3    Fully automatic page segmentation, but no OSD. (Default)
  4    Assume a single column of text of variable sizes.
  5    Assume a single uniform block of vertically aligned text.
  6    Assume a single uniform block of text.
  7    Treat the image as a single text line.
  8    Treat the image as a single word.
  9    Treat the image as a single word in a circle.
 10    Treat the image as a single character.
 11    Sparse text. Find as much text as possible in no particular order.
 12    Sparse text with OSD.
 13    Raw line. Treat the image as a single text line,
"""

"""
OCR engine mode
0 Legacy engine only
1 Neural nets LSTM engine only
2 Legacy + LSTM engines
3 Default, base on what is avaliable
"""

# change your number of page segmentation mode or OCR engine mode here
myconfig = r"--psm 3 --oem 3"

# extract string from images
text = pytesseract.image_to_string(PIL.Image.open("./data/chapter-1_page3.jpg"), config=myconfig)
print(text)

# output written into txt file
# with open("output.txt", "a") as file:
#     file.write(f"{text}\n")

# code for drawing rectangle around the texts, using openCV python package
# img = cv2.imread("./data/chapter-1_page3.jpg")
# height, width, _ = img.shape
#
# boxes = pytesseract.image_to_boxes(img, config=myconfig)
#
# for box in boxes.splitlines():
#     box = box.split(" ")
#     img = cv2.rectangle(img, (int(box[1]), height-int(box[2]), int(box[3]), height-int(box[4])), (0, 255, 0), 2)
#
# cv2.imshow("img", img)
# cv2.waitKey(0)