import cv2 as cv

# draw a rectangle bounding box with mouse

def draw_rectange(event, x, y, flags, param):

    list_cor = []

    if event == cv.EVENT_LBUTTONDOWN:
        start = (x, y)
        print(start)

    if event == cv.EVENT_LBUTTONUP:
        end = (x, y)
        print(end)

    
        cv.rectangle(image, start, end, (0, 255, 0), 2)
        cv.imshow("image", image)


image = cv.imread("data/file1.jpg")
cv.imshow("image", image)
cv.setMouseCallback("image", draw_rectange)
cv.waitKey(0)
cv.destroyAllWindows()
