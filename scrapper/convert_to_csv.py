import os
import json
import csv

data_to_export = []

def get_dict(data, category):
    d = []
    for key in data.keys():
        try:
            d.append({
                "Product ID": key,
                "Categories": category,
                "Name *": data[key]["name"].encode('utf-8').decode('utf-8'),
                "Price tax excluded": round(data[key]["price"] / 1.23, 2),
                "Price tax included": data[key]["price"],
                "Image URLs (x,y,z...)": "null",
                "Description": data[key]["description"].encode('utf-8').decode('utf-8'),
                "Feature(Name:Value:Position)": "Kolor:" + data[key]["color"].encode('utf-8').decode('utf-8') + ":0",
            })
        except:
            pass
    return d
    

csv_dictwriter = csv.DictWriter(open("../scrapper-results/data.csv", "w", newline='', encoding='utf-8'), fieldnames=["Product ID", "Categories", "Name *", "Price tax excluded", "Price tax included", "Image URLs (x,y,z...)", "Description", "Feature(Name:Value:Position)"], delimiter=";")

csv_dictwriter.writeheader()

def write_to_csv(filename, category):
    file = open("../scrapper-results/" + filename + ".json", "r")
    data = json.load(file)

    data_to_export = get_dict(data, category)

    for row in data_to_export:
        csv_dictwriter.writerow(row)

    file.close()

write_to_csv("mezczyzni-buty", "Mężczyźni, Buty")
write_to_csv("mezczyzni-odziez", "Mężczyźni, Ubrania")
write_to_csv("mezczyzni-akcesoria", "Mężczyźni, Akcesoria")
write_to_csv("kobiety-buty", "Kobiety, Buty")
write_to_csv("kobiety-odziez", "Kobiety, Ubrania")
write_to_csv("kobiety-akcesoria", "Kobiety, Akcesoria")
write_to_csv("chlopcy-buty", "Dzieci, Buty dla chłopców")
write_to_csv("dziewczynki-buty", "Dzieci, Buty dla dziewczynek")
write_to_csv("dzieci-akcesoria", "Dzieci, Akcesoria")
write_to_csv("buty-pilka_nozna", "Sport, Buty piłkarskie")
write_to_csv("buty-bieganie", "Sport, Buty biegowe")