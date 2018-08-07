from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import json

# TODO: more restaurants
# TODO: figure out the way to do this daily and see the results in some better way
# TODO: consider github pages as possible hosting for website


# Decide which sections should not be printed
def shouldIncludeSection(sectionHeader):
    return not ('Salads' in sectionHeader or 'Sauces' in sectionHeader)


# Print the daily offer
def printDailyOffer(sectionHeader, sectionPrice, sectionOffers):
    print(sectionHeader + ', ' + sectionPrice)
    for offer in sectionOffers.findAll('li'):
        print('   -' + offer.h3.text)
    print()

def prepareJson(sectionHeader, sectionPrice, sectionOffers):
    offers = []
    for offer in sectionOffers.findAll('li'):
        offers.append((offer.h3.text))
    
    with open("daily-offer.json", "a") as f:
        json.dump({"name": sectionHeader, "price": sectionPrice, "offers": offers}, f, indent=2)
        if not (sectionHeader == "Om\u00e1\u010dky"):
            f.write(",")

# Get the whole offer for today
def getDailyOffer():

    jsonOfferObjects = []

    with open("daily-offer.json", "w+") as f:
        f.write("{\"dailyOffer\": [")

    for section in page_soup.findAll("section"):
        sectionHeader = section.strong.text

        if not shouldIncludeSection(sectionHeader):
            continue
        else:
            sectionPrice = section.span.text
            sectionOffers = section.ul
            jsonOfferObjects.append(prepareJson(sectionHeader, sectionPrice, sectionOffers))

    with open("daily-offer.json", "a") as f:
        f.write("]}")


prestoURL = 'http://www.prestorestaurant.cz/cz/click/chodov/1/'

# Opening the page and grabbing the content
uClient = uReq(prestoURL)

# Stores the source code in page_html variable
page_html = uClient.read()

# Closes the connection
uClient.close()

# Tells BeautifulSoup how to parse the provided data
page_soup = soup(page_html, "html.parser")

# Get the offer for today
getDailyOffer()
