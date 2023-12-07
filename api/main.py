import random
from prestapyt import PrestaShopWebServiceError
from prestapyt import PrestaShopWebService
from prestapyt import PrestaShopWebServiceDict

from monkey import _execute
from debug import Debug

from multiprocessing import Pool

import csv
import urllib3


SHOP_URL = 'https://localhost'
SHOP_KEY = '8BH9TRT89TMVM3LDJGDYFMPDRLHJTE6N'

PrestaShopWebService._execute = _execute
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

class DataHandler:
    def __init__(self):
        self.data = []
        self.field_names = ["Product ID", "Categories", "Name *", "Price tax excluded", "Price tax included", "Image URLs (x,y,z...)", "Description", "Feature(Name:Value:Position)", "Count"]
        self.read_csv()

    def read_csv(self):
        with open('scrapper-results/data.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                self.data.append(row)

    def get_data(self):
        return self.data

class PrestaHandler:
    def __init__(self):
        self.api = PrestaShopWebServiceDict(SHOP_URL, SHOP_KEY)
        self.api.debug = True

    def search_categories(self, name):
        categories = self.api.search('categories', options={'filter[name]' : name})
        return categories
    
    def get_category(self, name):
        try:
            if not is_integer(name):
                return self.search_categories(name)[0]
            else:
                return str(name)
        except IndexError:
            # throw exception
            with open("log.txt", "a") as file:
                file.write("Category not found: " + name + "\n")

    def get_products(self):
        products = self.api.search('products')
        return products
    
    def get_product(self, id):
        product = self.api.get('products', id)
        return product
    
    def add_product(self, product):
        new_product = self.api.add('products', product)
        Debug()("id:", new_product["prestashop"]["product"]["id"])
        return new_product["prestashop"]["product"]["id"]
    
    def add_feature(self, feature):
        new_feature = self.api.add('product_features', feature)
        return new_feature
    
    def add_feature_value(self, feature_value):
        new_feature_value = self.api.add('product_feature_values', feature_value)
        return new_feature_value
    
    def get_feature_value_id(self, id, name):
        feature_values = self.api.search('product_feature_values', options={'filter[value]' : name})
        Debug()(feature_values)
        if len(feature_values) == 0:
            self.add_feature_value({
                    "product_feature_value" : {
                        "id_feature" : str(id),
                        "custom" : str(0),
                        "value" : {"language" : {
                            "value" : name,
                            "attrs" : {
                                "id" : str(1)
                            }}}}
                })
            feature_value_id = self.get_feature_value_id(id, name)
            return feature_value_id
        else:
            feature_value_id = feature_values[0]
            return feature_value_id
    
    def get_feature_id(self, name):
        features = self.api.search('product_features', options={'filter[name]' : name})
        Debug()(features)
        if len(features) == 0:
            self.add_feature({
                "product_feature" : {
                    "name" : {"language" : {
                        "value" : name,
                        "attrs" : {
                            "id" : str(1)
                        }}}}
            })
            feature_id = self.get_feature_id(name)
            return feature_id
        else:
            feature_id = features[0]     
            return feature_id
        
    def update_stock(self, id, quantity):
        stock = self.api.get('stock_availables', id)
        stock['stock_available']['quantity'] = quantity
        ret = self.api.edit('stock_availables', stock)
        Debug()("quantity:", ret["prestashop"]["stock_available"]["quantity"])

    def add_image(self, id, image_content, image_name):
        new_image = self.api.add("/images/products/" + str(id), files=[("image", image_name, image_content)])
        Debug()(new_image["prestashop"]["image"]["id"])


def process_product(product):
    handler = PrestaHandler()
    product_id = product['Product ID']
    product_name = product['Name *']
    product_price_tax_excluded = product['Price tax excluded']
    product_price_tax_included = product['Price tax included']
    
    product_description = product['Description']
    product_category = product['Categories']
    product_image = product['Image URLs (x,y,z...)'].split(',')[0].split('/')[-1]
    product_image_small = product['Image URLs (x,y,z...)'].split(',')[1].split('/')[-1]
    product_feature = product['Feature(Name:Value:Position)']
    product_count = product['Count']

    feature_id = handler.get_feature_id(product_feature.split(':')[0])
    feature_value_id = handler.get_feature_value_id(feature_id, product_feature.split(':')[1])
    
    new_product = {
        "product" : {
            "name" : {"language" : {
                "value" : product_name,
                "attrs" : {
                    "id" : str(1)
                }}},
            "price" : str(product_price_tax_excluded),
            "description" : {"language" : {
                "value" : product_description,
                "attrs" : {
                    "id" : str(1)
                }}},
            "wholesale_price" : str(product_price_tax_excluded),
            "active" : str(1),
            "id_tax_rules_group" : str(1),
            "id_category_default" : handler.get_category(product_category.split(', ')[0]),
            "state": str(1),
            "associations" : {
                "categories" : {
                    "category" : {
                        "id" : handler.get_category(product_category.split(', ')[1])
                    },
                },
                "product_features" : {
                    "product_feature" : {
                        "id" : str(feature_id),
                        "id_feature_value" : str(feature_value_id),
                    }
                },
            }
        }
    }

    product_id = handler.add_product(new_product)

    handler.update_stock(product_id, product_count)
    with open('./scrapper-results/images/' + product_image, 'rb') as file:
        handler.add_image(product_id, file.read(), product_image)
    with open('./scrapper-results/images/' + product_image_small, 'rb') as file:
        handler.add_image(product_id, file.read(), product_image_small)

    print("Added product: " + product_name)     

def main():
    data_handler = DataHandler()

    with Pool(30) as p:
        p.map(process_product, data_handler.get_data())
        


if __name__ == '__main__':
    main()  