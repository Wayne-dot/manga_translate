import cv2 as cv

# draw a rectangle bounding box with mouse

def draw_rectange(event, x, y, flags, param):
    

    if event == cv.EVENT_LBUTTONDOWN:
        print("left is press")

    if event == cv.EVENT_LBUTTONUP:
        print("left is release")



    # cv.rectangle()
    # cv.imshow()


image = cv.imread("data/file1.jpg")
cv.imshow("image", image)
cv.setMouseCallback("image", draw_rectange)
cv.waitKey(0)
cv.destroyAllWindows()
