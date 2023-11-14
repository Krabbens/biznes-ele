import time
from selenium import webdriver

from SearchByNameAndAddRandomFoundToCart import SearchByNameAndAddRandomFoundToCart
from AddRandomFromCategoriesToCart import AddRandomFromCategoriesToCart

website_addr = "http://localhost:8080/"
all_products = "index.php?id_category=2&controller=category"

if __name__ == '__main__':
    start_time = time.time()
    browser = webdriver.Chrome()

    # 4a.
    add_x_random_from_y_categories_to_cart = AddRandomFromCategoriesToCart(website_addr+all_products, browser, 10, 2)
    add_x_random_from_y_categories_to_cart.run()

    # 4b.
    search_by_name_and_add_random_found_to_cart = SearchByNameAndAddRandomFoundToCart(website_addr, browser)
    # search_by_name_and_add_random_found_to_cart.run("humming")

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Czas wykonania: {elapsed_time} sekundy")

