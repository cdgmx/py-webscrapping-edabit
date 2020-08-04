#pip install BeautifulSoup
#pip install selenium
#pip install webdriver_manager


import discord
from  discord.ext import commands

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
#page_soup = soup(browser.page_source, "html.parser")
client = commands.Bot(command_prefix = '!')

@client.event

async def on_ready():
    print("ready")

#used lmxl to parse data
page_soup2 = soup(browser.page_source, 'lxml')


#match = page_soup2.find('div', class_='ui divided selection very relaxed middle aligned list')


# headline = []
# description = []
x = 0
for match in page_soup2.find_all('div', class_='item no-highlight'):

    headline = match.a.h3.text
    description = match.a.div.text

    print(headline)  
    print(description)
    print(x)
    x+=1



@client.command()
async def chall(ctx):

    for y in range(x):
        await ctx.send(headline[y] + "\n" +description[y]+ "\n")

client.run('NzQwMTA1OTQxMzkwOTgzMjIx.XykLXg.zEdSWMh83dpbZSynrPcdtTynQS4')












#main_file = page_soup.find_all("div", class_="item no-highlight")

#main_file = page_soup.find_all("div", class_="ui divided selection very relaxed middle aligned list")





#print(main_file)


#for each_div in page_soup.findAll('div',{'class':'ui divided selection very relaxed middle aligned list'}):
    #print(each_div)




#printing the pagesource with condition of finding all div only with a class of "name of a class"
#print(main_file)

