from definitions import Definitions
from scraper import SeleniumScraper
from selenium.webdriver.common.by import By
from pprint import pprint
import concurrent.futures
import json
from PIL import Image
from base64 import b64encode
from io import BytesIO
import requests

class Client:
    def __init__(self, scraper: SeleniumScraper):
        self.scraper = scraper

    def process_boot(self, _id):
        try:
            PATH_TO_CHROMEDRIVER = "here insert path to chromedriver"
            scp = SeleniumScraper(PATH_TO_CHROMEDRIVER, headless=False)
            scp.visit("https://adidas.pl/api/search/product/" + _id)
            js = scp.driver.page_source.split(";\">")[1].split("</pre>")[0]
            parsed = json.loads(js)

            img_content = requests.get(parsed['images'][0]['src'])

            new_dict = {
                _id: {
                    "name": parsed['name'],
                    "color": parsed['color'],
                    "model": parsed['modelId'],
                    "price": parsed['price'],
                    "salePrice": parsed['salePrice'],
                    "image_full": self.convert_to_b64(600, 600, img_content),
                    "image_thumb": self.convert_to_b64(256, 256, img_content),
                    "gender": parsed['gender']
                }
            }

            return new_dict
        except:
            return {}
        
    def convert_to_b64(self, width, height, response):
        img = Image.open(BytesIO(response.content))
        img = img.resize((width, height))
        buffered = BytesIO()
        img.save(buffered, format="JPEG")
        return b64encode(buffered.getvalue()).decode('utf-8')

    def get_site(self, site):
        boots = {}
        for i in range(3):
            print("Page: " + str(i))
            self.scraper.visit(site + "?start=" + str(i * 48))
            # wait for 2 seconds
            self.scraper.driver.implicitly_wait(2)
            boots_cards = self.scraper.from_class_name(Definitions.CLASS_BOOTS_CARD)
            for card in boots_cards:
                try:
                    _id = card.find_element(By.CLASS_NAME, Definitions.CLASS_HOCKEYCARD).get_attribute('href').split("/")[-1].split(".html")[0]
                    boots[_id] = {
                        "category": card.find_element(By.CLASS_NAME, Definitions.CLASS_CARD_CATEGORY).get_attribute('innerHTML')
                    }
                except:
                    print("error")
            # for every id in parallel
            with concurrent.futures.ThreadPoolExecutor(max_workers=12) as executor:
                futures = [executor.submit(self.process_boot, _id) for _id in boots.keys()]
                concurrent.futures.wait(futures)
                results = [future.result() for future in futures]
                for result in results:
                    boots.update(result)
        
        with open("../scrapper-results/" + site.split("/")[-1] + '.json', 'w') as outfile:
            json.dump(boots, outfile)

    def get_men_boots(self):
        self.get_site("https://www.adidas.pl/mezczyzni-buty")

    def get_woman_boots(self):
        self.get_site("https://www.adidas.pl/kobiety-buty")

    def get_men_clothes(self):
        self.get_site("https://www.adidas.pl/mezczyzni-odziez")

    def get_woman_clothes(self):
        self.get_site("https://www.adidas.pl/kobiety-odziez")

    def get_men_accessory(self):
        self.get_site("https://www.adidas.pl/mezczyzni-akcesoria")

    def get_woman_accessory(self):
        self.get_site("https://www.adidas.pl/kobiety-akcesoria")

    def get_soccer_boots(self):
        self.get_site("https://www.adidas.pl/buty-pilka_nozna")
    
    def get_running_boots(self):
        self.get_site("https://www.adidas.pl/buty-bieganie")

    def get_children_boots(self):
        self.get_site("https://www.adidas.pl/chlopcy-buty")
        self.get_site("https://www.adidas.pl/dziewczynki-buty")

    def get_children_accessory(self):
        self.get_site("https://www.adidas.pl/dzieci-akcesoria")