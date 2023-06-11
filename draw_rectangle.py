import cv2 as cv
import numpy as np
from PIL import Image
import pytesseract
import time

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Wayne\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

# write documentation

# draw a rectangle bounding box with mouse


class draw_bounding_box:
    def __init__(self):
        self.corrdinate = []
        self.start = ()
        self.image = None

    def draw_rectange(self, event, x, y, flags, param):

        if event == cv.EVENT_LBUTTONDOWN:
            self.start = (x, y)
            self.corrdinate.append(self.start)

        if event == cv.EVENT_LBUTTONUP:
            end = (x, y)
            self.corrdinate.append(end)
            # print(end)
            cv.rectangle(self.image, self.start, end, (0, 255, 0), 2)
            cv.imshow("image", self.image)
    
    def run(self, image_path):
        self.image = cv.imread(image_path)
        # convert to grey image
        # grey = cv.cvtColor(self.image, cv.COLOR_BGR2GRAY)
        cv.imshow("image", self.image)


        # # cv.adaptiveThreshold(grey_img, 255, thresholding style, method, size_of_area (must be odd number), constatn substract from weight_mean)
        # grey = cv.adaptiveThreshold(grey, 255, cv.THRESH_BINARY, cv.ADAPTIVE_THRESH_GAUSSIAN_C, 71, 10)

        # # flip binary value
        # grey = cv.bitwise_not(grey)
        # # remove boundary for word
        # # kernal = matrix around the object
        # # np.ones((row, column), 8-bit unsigned integer (0 to 255))
        # # [[1, 1],
        # # [1, 1]]
        # kernal = np.ones((3, 3), np.uint8)
        # grey = cv.erode(grey, kernal)
        
        # # flip binary image
        # grey = cv.bitwise_not(grey)
        # cv.imwrite("save.jpg", grey)







        # # find the text
        # counters, hierarchy  = cv.findContours(grey, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        # prund_counters = []
        # mask = np.zeros_like(self.image)
        # mask = cv.cvtColor(mask, cv.COLOR_BGR2GRAY)
        # height, width, channel = self.image.shape

        # for counter in counters:
        #     x, y, w, h = cv.boundingRect(counter)
        #     cut = grey[y: y+h, x:x+w]
        #     text = pytesseract.image_to_string(cut)

        #     if text.strip():
        #         print(f"Contour found {text}")


        # # new = cv.drawContours(mask, prund_counters, -1, (255,255,255), 1)
        

        # # cv.imshow("new", new)
        # # cv.imwrite("new.jpg", new)



        # # draw counter again inside new image
        # # counters2, hierarchy2 = cv.findContours(new, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        # # pil_image = Image.fromarray(new_image)
        # # text = pytesseract.image_to_string(pil_image, lang="eng")
        # # print(text)

        cv.setMouseCallback("image", self.draw_rectange)
        cv.waitKey(0)
        cv.destroyAllWindows()



bounding_box = draw_bounding_box()
bounding_box.run("data/chapter-1_page1.jpg")
