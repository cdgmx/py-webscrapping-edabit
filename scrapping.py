#pip install BeautifulSoup
#pip install selenium
#pip install webdriver_manager



from bs4 import BeautifulSoup as soup

from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

#this is to ensure that all items on the website is loaded.
#some website uses js to load some of its parts, since selenium only request text strings from a website, it connnot execute js files to extract strings that's why we need to have a webdriver to execute the js first before extracting txt strings.

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#this is to ensure that we are running the latest driver manager (uses chrome, can use firefox but i dont know the syntax)
browser = webdriver.Chrome(ChromeDriverManager().install())

#paste your url here
my_url = "https://edabit.com/challenges"

#http get request
browser.get(my_url)

#wait for a certain class(can be an element) to load before scrapping the data, with waiting time of 10 secs
myElem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'description')))

#parse the page source as html file
page_soup = soup(browser.page_source, "html.parser")


#printing the pagesource with condition of finding all div only with a class of "name of a class"
print(page_soup.find_all("div", class_="ui divided selection very relaxed middle aligned list"))

