import cv2 as cv

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
        cv.imshow("image", self.image)
        cv.setMouseCallback("image", self.draw_rectange)
        cv.waitKey(0)
        cv.destroyAllWindows()



bounding_box = draw_bounding_box()
bounding_box.run("data/file1.jpg")
print(bounding_box.corrdinate)

