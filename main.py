import requests
import cloudscraper
import re
import json
from colorama import Fore
scraper = cloudscraper.create_scraper(
    browser={
        'browser': 'chrome',
        'platform': 'android',
        'desktop': False
    }
)
def get_results(url):
    response = scraper.get(url)
    #print(Fore.GREEN,"Test 1: Passed")
    return(response.text)
def parse_page(results):
    splitt = results.split("window.Quizlet")
    split = splitt[6].split("AdHeading AdHeading--right")
    call = split[0].split("QLoad")
    result = call[0].strip(";")
    result = result.strip('["MiniFlashcards"] = ')
    result = result.strip(';')
    results_json = json.loads(result)
    data = (results_json.get('studiableDocumentData'))
    suitable_items = data.get('studiableItems')
    return(suitable_items)
link = input("Enter quizlet link:   ")
mode = input("Choose a mode: [>>,<>,<<]")
results = (get_results(url=link))
suitable_items = parse_page(results=results)
for n in range(len(suitable_items)):
    card_sides = suitable_items[n].get('cardSides') ### CHANGE TO MOVE TO NEXT SLIDE
    question_side = card_sides[0].get('media')
    def_side = card_sides[1].get('media')
    question = (question_side[0].get('plainText'))
    answer = (def_side[0].get('plainText'))
    print(Fore.RESET,f"{question}{mode}{answer}")
