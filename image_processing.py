import cv2 as cv
import numpy as np

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
        self.height = self.image.shape[0]
        self.width = self.image.shape[1]

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
        
        grey = cv.bitwise_not(grey)
        cv.imshow("adopte", grey)



        cv.setMouseCallback("image", self.draw_rectange)
        cv.waitKey(0)
        cv.destroyAllWindows()



bounding_box = draw_bounding_box()
bounding_box.run("data/chapter-1_page3.jpg")
