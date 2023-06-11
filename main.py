import cv2 as cv

# draw a rectangle bounding box with mouse

def draw_rectange(event, x, y, flags, param):

    list_cor = []

    if event == cv.EVENT_LBUTTONDOWN:
        list_cor.append(x)
        list_cor.append(y)

    if event == cv.EVENT_LBUTTONUP:
        list_cor.append(x)
        list_cor.append(y)
        end = (x, y)
        print(end)

    
        cv.rectangle(image, (list_cor[0], list_cor[1]), (list_cor[2], list_cor[3]), (0, 255, 0), 2)
        cv.imshow("image", image)


image = cv.imread("data/file1.jpg")
cv.imshow("image", image)
cv.setMouseCallback("image", draw_rectange)
cv.waitKey(0)
cv.destroyAllWindows()
