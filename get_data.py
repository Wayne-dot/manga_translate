import requests
from bs4 import BeautifulSoup
import time
from tqdm import tqdm

for i in tqdm(range(182, 201)):
    URL = f"https://sololevelingmanga.org/manga/solo-leveling-chapter-{i}/"

    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")
    pictures_list = soup.find_all("img", class_="lazyload")


    for img in pictures_list:
        print(img)
        image_link = img["data-src"]
        try:
            image_response = requests.get(image_link)
        except:
            print("unable to connect")
        if image_response.status_code == 200:
            chapter_name = f"{img['alt'].split(' ')[2]}-{img['alt'].split(' ')[3]}"   
            page_number = img['alt'].split(' ')[6]
            name = f"{chapter_name}_page{page_number}" #Example: chapter-1_page3
            with open(f"data/{name}.jpg", "wb") as file:
                file.write(image_response.content)

                print("Image download successfully")
            time.sleep(5)
        else:
            print("Unable to download image, this might due to change in website html struture")

        print("---------------------------------------------------------------------------------------------")
        


# Output of the file
# ---------------------------------------------------------------------------------------------
# <img alt="Solo Leveling Chapter 81 - PAGE 40" class="lazyload" data-src="https://xvqiuawerl.imagemanga.online/aHR0cHM6Ly92Ny5ta2tsY2RudjZ0ZW1wdjMuY29tL2ltZy90YWJfNy8wMi85MS8xNy9kcjk4MDQ3NC9jaGFwdGVyXzgxLzQxLW4uanBn/aHR0cHM6Ly9yZWFkbWFuZ2FiYXQuY29tL3JlYWQtaXczODYzNjM%3D" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20210%20140%22%3E%3C/svg%3E"/>
# Image download successfully
# ---------------------------------------------------------------------------------------------
# <img alt="Solo Leveling Chapter 81 - PAGE 41" class="lazyload" data-src="https://xvqiuawerl.imagemanga.online/aHR0cHM6Ly92Ny5ta2tsY2RudjZ0ZW1wdjMuY29tL2ltZy90YWJfNy8wMi85MS8xNy9kcjk4MDQ3NC9jaGFwdGVyXzgxLzQyLW4uanBn/aHR0cHM6Ly9yZWFkbWFuZ2FiYXQuY29tL3JlYWQtaXczODYzNjM%3D" src="data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220%200%20210%20140%22%3E%3C/svg%3E"/>
# Image download successfully
# ---------------------------------------------------------------------------------------------