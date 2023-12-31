from scraper import SeleniumScraper
from client import Client
import json


if __name__ == "__main__":
    PATH_TO_CHROMEDRIVER = "here insert path to chromedriver"

    scraper = SeleniumScraper(PATH_TO_CHROMEDRIVER, headless=False)
    client = Client(scraper)

    categories = {
        "Mężczyźni": {
            "Buty": [],
            "Ubrania": [],
            "Akcesoria": []
        },
        "Kobiety": {
            "Buty": [],
            "Ubrania": [],
            "Akcesoria": []
        },
        "Dzieci": {
            "Buty dla chłopców": [],
            "Buty dla dziewczynek": [],
            "Akcesoria": []
        },
        "Sport": {
            "Buty biegowe": [],
            "Buty piłkarskie": [],
        }
    }

    with open('../scrapper-results/categories.json', 'w') as outfile:
        json.dump(categories, outfile)

    client.get_men_boots()
    client.get_woman_boots()
    client.get_men_clothes()
    client.get_woman_clothes()
    client.get_men_accessory()
    client.get_woman_accessory()
    client.get_soccer_boots()
    client.get_running_boots()
    client.get_children_boots()
    client.get_children_accessory()