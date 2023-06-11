import cv2 as cv

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

        th2 = cv.adaptiveThreshold(grey, 255, cv.THRESH_BINARY_INV, cv.ADAPTIVE_THRESH_GAUSSIAN_C, 101, 10)
        
        cv.imshow("adopte", th2)



        cv.setMouseCallback("image", self.draw_rectange)
        cv.waitKey(0)
        cv.destroyAllWindows()



bounding_box = draw_bounding_box()
bounding_box.run("data/chapter-1_page3.jpg")
print(bounding_box.corrdinate)
print(bounding_box.height)
print(bounding_box.width)

# process image
# # Issue - image too big
# maximum (700, 750)
