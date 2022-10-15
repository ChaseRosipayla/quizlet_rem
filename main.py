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
link = input("Enter quizlet link:   ")
results = (get_results(url=link))
splitt = results.split("window.Quizlet")
#print(Fore.GREEN,"Test 2: Passed")
#print(splitt[6])
split = splitt[6].split("AdHeading AdHeading--right")
#print(Fore.GREEN,"Test 3: Passed")
#print(split[0])
call = split[0].split("QLoad")
#print(Fore.GREEN,"Test 4: Passed")
#print(call[0])
result = call[0].strip(";")
#print(Fore.GREEN,"Test 5: Passed")
result = result.strip('["MiniFlashcards"] = ')
#print(Fore.GREEN,"Test 6: Passed")
result = result.strip(';')
#print(Fore.GREEN,"Test 7: Passed")
#print(result)
results_json = json.loads(result)
#print(Fore.GREEN,"Test 8: Passed")
#print(results_json)
data = (results_json.get('studiableDocumentData'))
#print(Fore.GREEN,"Test 9: Passed")
suitable_items = data.get('studiableItems')
#print(Fore.GREEN,"Test 10: Passed")
for n in range(len(suitable_items)):
    card_sides = suitable_items[n].get('cardSides') ### CHANGE TO MOVE TO NEXT SLIDE
    question_side = card_sides[0].get('media')
    def_side = card_sides[1].get('media')
    question = (question_side[0].get('plainText'))
    answer = (def_side[0].get('plainText'))
    print(Fore.RESET,f"{question}>>{answer}")
#print(Fore.GREEN,"Test 11: Finished")