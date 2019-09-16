# Import libraries
# import requests
# import urllib.request
# import time
# from bs4 import BeautifulSoup

def scrapeEmag(link):
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

    print(titleValue)
    print(priceValue)

# link = "https://www.emag.ro/telefon-mobil-samsung-galaxy-note-10-plus-dual-sim-256gb-12gb-ram-4g-aura-glow-sm-n975fzsdrom/pd/DGXRJ5BBM/?ref=fam#Aura-Glow"

# scrapeEmag(link)


