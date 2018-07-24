from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# TODO: more restaurants
# TODO: figure out the way to do this daily and see the results in some better way
# TODO: consider github pages as possible hosting for website


# Decide which sections should not be printed
def shouldPrint(sectionHeader):
    return not ('Saláty' in sectionHeader or 'Omáčky' in sectionHeader)


# Print the daily offer
def printDailyOffer(sectionHeader, sectionPrice, sectionOffers):
    print(sectionHeader + ', ' + sectionPrice)
    for offer in sectionOffers.findAll('li'):
        print('   -' + offer.h3.text)
    print()


# Get the whole offer for today
def getDailyOffer():
    for section in page_soup.findAll("section"):
        sectionHeader = section.strong.text

        if not shouldPrint(sectionHeader):
            continue
        else:
            sectionPrice = section.span.text
            sectionOffers = section.ul
            printDailyOffer(sectionHeader, sectionPrice, sectionOffers)


presto = 'http://www.prestorestaurant.cz/cz/click/chodov/1/'

# Opening the page and grabbing the content
uClient = uReq(presto)

# Stores the source code in page_html variable
page_html = uClient.read()

# Closes the connection
uClient.close()

# Tells BeautifulSoup how to parse the provided data
page_soup = soup(page_html, "html.parser")

# Get the offer for today
getDailyOffer()
