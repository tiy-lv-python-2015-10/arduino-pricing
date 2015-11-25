import requests as r
from bs4 import BeautifulSoup
from pymongo import MongoClient
import pymongo

response = r.get("https://www.adafruit.com/category/17")
soup = BeautifulSoup(response.content, 'html.parser')

client = MongoClient()
db = client.test
db.arduinos

def arduino():
    ##### FIND PRODUCT ID'S #######
    product_id = soup.find_all('div', class_='product_id', )
    for product in product_id:
        print(product.contents[0])
        result = db.arduino.insert_one(
        {
           '_id': product.contents[0],
        }
        )

    ##### FIND PRICES #######
    prices = soup.find_all('span', class_='normal-price', )
    for price in prices:
        print(price.contents[0])
        db.arduino.insert_one(
        {
           'price': price.contents[0],
        }
        )

    ##### FIND NAMES #######
    names = soup.find_all('a', class_='ec_click_product', )
    for name in names:
        print(name.contents[0])
        print(name['href'])
        db.arduino.insert_one(
        {
            'name': name.contents[0],
            'detail_page': name['href']
        }
        )

    ##### FIND ITEMS IN STOCK #######
    stocks = soup.find_all('div', class_='stock', )
    for stock in stocks:
        if stock.contents[0] == "IN STOCK":
            print(0)
        print(stock.contents[0])
        db.arduino.insert_one(
        {
           'stock': stock.contents[0],
        }
        )


    ##### FIND IMAGE URLS #######
    images = soup.find_all('div', class_='img-container', )
    for img in images:
        db.arduino.insert_one(
        {
            "img_url": img.a['href'],

        }
        )
        # print(img.a['href'])

def search_price(price):
    client = MongoClient()
    db = client.arduino
    cursor = db.arduino.find({'price': price})
    return cursor

def search_products(name):
    client = MongoClient()
    db = client.arduino
    cursor = db.arduino.find({'name': name})
    return cursor

if __name__ == '__main__':
    arduino()
    search_price("$12.50")
    search_products("Arduino Uno R3 (Atmega328 - assembled)")


