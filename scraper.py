from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# TODO: more restaurants
# TODO: figure out the way to do this daily and see the results in some better way

presto = 'http://www.prestorestaurant.cz/cz/chodov/'
# Opening the page and grabbing the content
uClient = uReq(presto)
# Stores the source code in page_html variable
page_html = uClient.read()
# Closes the connection
uClient.close()
# Tells BeautifulSoup how to parse the provided data
page_soup = soup(page_html, "html.parser")
# Grabs each section with class "list-new" and "red-section"
main_courses = page_soup.findAll("section", {"class":"list-new"})
daily_offers = page_soup.findAll("section", {"class":"red-section"})
# Selects just main course and daily offers from those sections above
course = main_courses[0].findAll("h3")
daily_offer = daily_offers[1].findAll("h3")
# If there is something in main courses, loops through each meal from main courses and prints it on sepate lines
if len(course) > 0:
    print('Hlavni jidla:')
    for meal in course:
        print(meal.text)
else:
    print('Dnes neni nic v sekci "Hlavni jidla"')
print('')
# If there is something in daily offer, loops through each meal from daily offers and prints it on sepate lines
if len(daily_offer) > 0:
    print('Denni nabidka:')
    for meal in daily_offer:
        print(meal.text)
else:
    print('Dnes neni nic v sekci "Denni nabidka"')
