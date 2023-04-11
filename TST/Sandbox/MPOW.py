import requests
from bs4 import BeautifulSoup
import os
from urlextract import URLExtract

url = "https://mars.nasa.gov/mars2020/multimedia/raw-images/image-of-the-week/"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
images = soup.find('div', class_="main_image")

# print(images)
# image_url = urlparse(str(images))
extractor = URLExtract()
urls = extractor.find_urls(str(images))
print(urls)
image_data = requests.get(urls[0]).content

with open("MPOW_current.jpg", "wb") as handler:
    handler.write(image_data)