import requests
import cv2

# Issue - image too big
# maximum (700, 750)

URL = "https://leveling-solo.net/manga/the-solo-leveling-chapter-1/"

image = cv2.imread("data/file1.jpg")
height = image.shape[0]
width = image.shape[1]