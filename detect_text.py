import cv2
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Wayne\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"


image = cv2.imread("data/chapter-1_page1.jpg")

# Preprocessing image - more clear  text
# Threshold
_, thres = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY)

kernal = np.ones((1, 1), np.uint8)

# Can't really see its purpose
# Remove Noise

# no_noise = cv2.morphologyEx(thres, cv2.MORPH_OPEN, kernel)

thres = cv2.cvtColor(thres, cv2.COLOR_RGB2GRAY)

result = cv2.connectedComponentsWithStats(thres, connectivity=8)
label_num = result[0]
label = result[1]
stats = result[2]

min_area = 100
text_region = []

for label in range(1, label_num):
    area = stats[label, cv2.CC_STAT_AREA]
    if area > min_area:
        print("detected")
        x, y, w, h = stats[label, cv2.CC_STAT_LEFT], stats[label, cv2.CC_STAT_TOP], stats[label, cv2.CC_STAT_WIDTH], stats[label, cv2.CC_STAT_HEIGHT]
        text_region.append((x, y, w, h))

img = cv2.cvtColor(thres, cv2.COLOR_GRAY2BGR)
for reg in text_region:
    x, y, w, h = reg
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("thres", thres)
cv2.imshow("modify", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Text detection
# text = pytesseract.image_to_string(no_noise, "eng")
# print(text)