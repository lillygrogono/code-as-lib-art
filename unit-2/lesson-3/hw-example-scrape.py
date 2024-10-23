import requests
from bs4 import BeautifulSoup

crgslist_response = requests.get("https://fonts.mojomox.com/blogs/on-type/free-bubble-fonts-google-fonts")

crgslist_soup_html = BeautifulSoup(crgslist_response.text, "html.parser")

crgslist_text = crgslist_soup_html.get_text()

freeStuff = []

def getTitles(soupdata):
    body = soupdata.select("body")
    if body:
        for b in body:
            freeStuff.append(soupdata.get_text())

getTitles(crgslist_soup_html)

freeText = " ".join(freeStuff)

crgslist_data = open('crgslist_free.txt', 'w')
crgslist_data.write(freeText)
crgslist_data.close()