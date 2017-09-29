from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

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
course = main_courses[0]
daily_offer = daily_offers[1]
print('Hlavni jidla:')
# Loops through each meal from main courses and prints it on sepate lines
for course in course.findAll("h3"):
    print(course.text)
print('')
# Loops through each meal from daily offers and prints it on sepate lines 
print('Denni nabidka:')
for meal in daily_offer.findAll("h3"):
    print(meal.text)
