from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'http://www.prestorestaurant.cz/cz/chodov/'
# Opening the page and grabbing the content
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
# Grabs each section with class "list-new"
main_courses = page_soup.findAll("section", {"class":"list-new"})
daily_offers = page_soup.findAll("section", {"class":"red-section"})
# Selects just main course from those sections
course = main_courses[0]
daily_offer = daily_offers[1]
print('Hlavni jidla:')
# Loops through each meal and prints it on sepate lines
for course in course.findAll("h3"):
    print(course.text)
print('')
print('Denni nabidka:')
for meal in daily_offer.findAll("h3"):
    print(meal.text)
