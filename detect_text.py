from easyocr import *

reader = easyocr.Reader(["en"])

# for i in range(1, 28):
result = reader.readtext(f"./data/chapter-1_page9.jpg")

# Replace 'output.txt' with the name you want for the output text file
with open('output.txt', 'w', encoding='utf-8') as file:
    for detection in result:
        text = detection[1]
        file.write(text + '\n')

print("Text extracted and saved to output.txt")