import requests
from bs4 import BeautifulSoup
import cloudscraper
scraper = cloudscraper.create_scraper()
link = input("Quizlet Link")
method = input("Choose a method, <<, >> , <>")
response = scraper.get(url=link)
#print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')

div = soup.findAll('div', {'class': 'SetPageTerm-sideContent'})
for n in range(len(div)):
    t1 = div[n].text
    try:
        t2 = div[n+1].text
    except:
        break
    print(f'{t1}{method}{t2}')
    #print(div.findAll('div', {'class': 'SetPageTerm-sideContent'}))
    #print(str(div).strip('<div class="SetPageTerm-sideContent"><a class="SetPageTerm-wordText"><span class='))
#print(soup.find("TermText notranslate lang-en").text)
#for link in soup.findAll('class="TermText notranslate lang-en"'):
   # print(link)