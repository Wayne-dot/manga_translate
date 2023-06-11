import requests
import cv2
from bs4 import BeautifulSoup

# Issue - image too big
# maximum (700, 750)

URL = "https://leveling-solo.net/manga/the-solo-leveling-chapter-1/"

# separator

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
pictures_list = soup.find_all("div", "separator")

for div in pictures_list:
    link = div.find("a")
    print(link["href"])
    break

image = cv2.imread("data/file1.jpg")
height = image.shape[0]
width = image.shape[1]