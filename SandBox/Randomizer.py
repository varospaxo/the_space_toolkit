import requests
from bs4 import BeautifulSoup
import os

from urlextract import URLExtract
url = "https://apod.nasa.gov/apod/random_apod.html"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
iframe = soup.find_all("iframe")
# iframe_src = iframe["src"]

print(iframe)
# image_url = urlparse(str(images))
extractor = URLExtract()
urls = extractor.find_urls(str(iframe))
print(urls)
image_data = requests.get(urls[0]).content

with open("image.jpg", "wb") as handler:
    handler.write(image_data)