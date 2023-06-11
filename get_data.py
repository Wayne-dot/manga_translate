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
    a = div.find("a")
    link = a["href"]
    manga_name = link.split("/")[5]
    chapter = link.split("/")[6]
    page = int(link.split("/")[7].split(".")[0])
    # page need to be -1
    
    img = requests.get(link)
    with open(f"data/chapter{chapter}_page{page-1}.jpg", "wb") as file:
        file.write(img.content)
    
