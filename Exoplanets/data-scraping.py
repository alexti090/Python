from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

STARTURL = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser = webdriver.Chrome('Path to the chrome driver.exe')
browser.get(STARTURL)
time.sleep(10)

def scrape():
  headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]
  planetData = []
  for i in range(444):
    soup = BeautifulSoup(browser.page_source, "html.parser")
    for ul_tag in soup.find_all("ul", attrs={'class': "exoplanet"}):
      li_tags = ul_tag.find_all("li")
      tempList = []
      for index, li_tag in enumerate(li_tags):
        if index == 0:
          tempList.append(li_tag.find_all('a')[0].contents[0])
        else:
          try:
            tempList.append(li_tag.contents[0])
          except:
            tempList.append('')
      planetData.append(tempList)
