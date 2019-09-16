# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# Set the URL you want to webscrape from
url = "https://www.emag.ro/telefon-mobil-samsung-galaxy-note-10-plus-dual-sim-256gb-12gb-ram-4g-aura-glow-sm-n975fzsdrom/pd/DGXRJ5BBM/?ref=fam#Aura-Glow"

# url = "http://example.com/"

# Connect to the URL
response = requests.get(url)

# Parse HTML and save to BeautifulSoup object
soup = BeautifulSoup(response.text, "html.parser")

priceHTMLTag = soup.find(class_="product-new-price")

priveValue = priceHTMLTag.contents[0]
priveValue = priveValue.strip()

print(priveValue)


