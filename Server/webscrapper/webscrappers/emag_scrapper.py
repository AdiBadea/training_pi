import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# Importing Functions
from functions.generateDateToday import generateDateToday

def scrapeEmag(link):

    scrapeResult = {"scrapeDate": "", "seller": "", "title": "", "price": ""}

    # Set the URL you want to webscrape from
    url = link
    # Connect to the URL
    response = requests.get(url)
    # Parse HTML and save to BeautifulSoup object
    soup = BeautifulSoup(response.text, "html.parser")

    # Get the title of the product
    productTitleHtmlTag = soup.find(class_="page-title")
    # Extract only the title innerhtml from the HTML Tag
    titleValue = productTitleHtmlTag.contents[0]
    # Delete whitespaces
    titleValue = titleValue.strip()

    # Get the HTML tag containing the price
    priceHTMLTag = soup.find(class_="product-new-price")
    # Extract only the price from the HTML Tag
    priceValue = priceHTMLTag.contents[0]
    # Delete whitespaces
    priceValue = priceValue.strip()

    scrapeResult["title"] = titleValue
    scrapeResult["price"] = priceValue
    scrapeResult["seller"] = "eMAG"
    scrapeResult["scrapeDate"] = str(generateDateToday())


    print(scrapeResult)


