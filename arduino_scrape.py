import re
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

response = requests.get('https://www.adafruit.com/category/17')
soup = BeautifulSoup(response.content, 'html.parser')
listings = soup.find_all('div', class_='row product-listing')
client = MongoClient()
db = client.arduino


def arduino_scrape_and_save():
    count = 0
    for listing in listings:
        product_id_string = listing.find('div', class_='product_id').string
        product_id = int(re.match('PRODUCT ID: (\d+)', product_id_string)
                         .group(1))
        name = listing.h1.string.strip()
        normal = listing.find('span', class_='normal-price')
        special = listing.find('span', class_='special-price')
        if normal:
            price_string = normal.string
            price = float(re.match(r'\$([.,\d]+)', price_string).group(1))
        elif special:
            price_string = special.string
            price = float(re.match(r'\$([.,\d]+)', price_string).group(1))
        else:
            price = 'none'

        detail_link = 'https://www.adafruit.com' + listing.h1.a['href']
        image_url = 'https://www.adafruit.com' + \
                    listing.find('a', class_='ec_click_product').img['src']
        out_of_stock = listing.find('span', class_='out-of-stock')
        if out_of_stock:
            stock = 0
        else:
            stock_string = listing.find('div', class_='stock').string.strip()
            if stock_string == 'IN STOCK':
                stock = 100
            else:
                stock = int(re.match(r'(\d+) IN STOCK', stock_string).group(1))

        db.products.insert_one(
            {
                '_id': product_id,
                'name': name,
                'price': price,
                'detail_link': detail_link,
                'stock': stock,
                'image_url': image_url,
            }
        )
        count += 1
    return count

if __name__ == '__main__':
    num_products = arduino_scrape_and_save()
    print("{} products added".format(num_products))
