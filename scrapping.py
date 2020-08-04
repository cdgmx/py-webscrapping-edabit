
from urllib.request import urlopen as uReq


from bs4 import BeautifulSoup as soup

from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


browser = webdriver.Chrome(ChromeDriverManager().install())


my_url = "https://edabit.com/challenges"
browser.get(my_url)

myElem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'description')))

page_soup = soup(browser.page_source, "html.parser")



print(page_soup.find_all("div", class_="ui divided selection very relaxed middle aligned list"))

