import time
from selenium import webdriver

from delete_products_from_cart import DeleteProductsFromCart
from go_to_cart_and_place_order import GoToCartAndPlaceOrder
from register_new_user import RegisterNewUser
from search_by_name_and_add_random_found_to_cart import SearchByNameAndAddRandomFoundToCart
from add_random_from_categories_to_cart import AddRandomFromCategoriesToCart
from check_order_status import CheckOrderStatusAndDownloadInvoice

website_addr = "https://localhost/"
all_products = "index.php?id_category=2&controller=category"
cart = "index.php?controller=cart"
register = "index.php?controller=authentication&create_account=1"

if __name__ == '__main__':
    start_time = time.time()
    browser = webdriver.Chrome()

    # 4a.
    add_x_random_from_y_categories_to_cart = AddRandomFromCategoriesToCart(website_addr + all_products, browser, 10, 2)
    add_x_random_from_y_categories_to_cart.run()

    # input("4a")

    # 4b.
    search_by_name_and_add_random_found_to_cart = SearchByNameAndAddRandomFoundToCart(website_addr, browser)
    search_by_name_and_add_random_found_to_cart.run("Ultraboost")

    # input("4b")

    # 4c.
    delete_products_from_cart = DeleteProductsFromCart(website_addr + cart, browser, 3)
    delete_products_from_cart.run()

    # input("4c")

    # 4d
    register_new_user = RegisterNewUser(website_addr+register, browser)
    register_new_user.run()

    # input("4d")

    # 4e,f,g,
    go_to_cart_and_place_order = GoToCartAndPlaceOrder(website_addr, browser)
    go_to_cart_and_place_order.run()

    # 4h, j
    check_order_status_and_download = CheckOrderStatusAndDownloadInvoice(website_addr, browser)
    check_order_status_and_download.run()

    # input("4j")

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Czas wykonania: {elapsed_time} sekundy")


