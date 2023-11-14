import time
from selenium import webdriver

from SearchByNameAndAddRandomFoundToCart import SearchByNameAndAddRandomFoundToCart

website_addr = "http://localhost:8080/"

if __name__ == '__main__':
    start_time = time.time()

    # 4b.
    search_by_name_and_add_random_found_to_cart = SearchByNameAndAddRandomFoundToCart(website_addr, webdriver.Chrome())
    search_by_name_and_add_random_found_to_cart.run("humming")

    end_time = time.time()
    elapsed_time = end_time - start_time

    search_by_name_and_add_random_found_to_cart.quitBrowser()
    print(f"Czas wykonania: {elapsed_time} sekundy")