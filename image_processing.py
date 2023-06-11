import cv2 as cv
import numpy as np
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"c:\Users\Wayne\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Tesseract-OCR"

# write documentation

# draw a rectangle bounding box with mouse


class draw_bounding_box:
    def __init__(self):
        self.corrdinate = []
        self.start = ()
        self.image = None
        self.height = None
        self.width = None

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
        grey = cv.cvtColor(self.image, cv.COLOR_BGR2GRAY)
        cv.imshow("image", self.image)


        # cv.adaptiveThreshold(grey_img, 255, thresholding style, method, size_of_area (must be odd number), constatn substract from weight_mean)
        grey = cv.adaptiveThreshold(grey, 255, cv.THRESH_BINARY, cv.ADAPTIVE_THRESH_GAUSSIAN_C, 71, 10)

        # flip binary value
        grey = cv.bitwise_not(grey)
        # remove boundary for word
        # kernal = matrix around the object
        # np.ones((row, column), 8-bit unsigned integer (0 to 255))
        # [[1, 1],
        # [1, 1]]
        kernal = np.ones((2, 2), np.uint8)
        grey = cv.erode(grey, kernal)
        
        # flip binary image
        grey = cv.bitwise_not(grey)

        # find the text
        counters, hierarchy  = cv.findContours(grey, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        prund_counters = []
        mask = np.zeros_like(self.image)
        mask = cv.cvtColor(mask, cv.COLOR_BGR2GRAY)
        height, width, channel = self.image.shape

        for counter in counters:
            area = cv.contourArea(counter)
            if area > 100 and area < ((height / 3) * (width / 3)):
                prund_counters.append(counter)

        new = cv.drawContours(mask, prund_counters, -1, (255,255,255), 1)

        # draw counter again inside new image
        counters2, hierarchy2 = cv.findContours(new, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        for counter2 in counters2:
            area = cv.contourArea(counter2)
            # search if there is big text
            if area > 1000 and area < ((height / 3) * (width / 3)):
                draw_mask = cv.cvtColor(np.zeros_like(self.image), cv.COLOR_BGR2GRAY)
                approx = cv.approxPolyDP(counter2, 0.01*cv.arcLength(counter2,True), True)

                cv.fillPoly(draw_mask, [approx], (255,0,0))
                new_image = cv.bitwise_and(draw_mask, cv.cvtColor(self.image, cv.COLOR_BGR2GRAY))
                # cv.imshow("new", new_image)

                y = approx[:, 0, 1].min()
                h = approx[:, 0, 1].max() - y
                x = approx[:, 0, 0].min()
                w = approx[:, 0, 0].max() - x
                new_image = new_image[y:y+h, x:x+w]

                cv.imshow("new", new_image)

                pil_image = Image.fromarray(new_image)
                text = pytesseract.image_to_string(pil_image, lang="kor")
                print(text)



        cv.imshow("adopte", grey)
        cv.setMouseCallback("image", self.draw_rectange)
        cv.waitKey(0)
        cv.destroyAllWindows()



bounding_box = draw_bounding_box()
bounding_box.run("data/chapter-1_page3.jpg")
