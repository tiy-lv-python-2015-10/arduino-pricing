import requests as r
from bs4 import BeautifulSoup

response = r.get("https://www.adafruit.com/category/17")
response.content
soup = BeautifulSoup(response.content, 'html.parser')

# Product ID
soup.find_all('div', 'product_id')

# Price
soup.find_all('span', 'normal-price')

# Name
# all names show and duplicate names
for link in soup.find_all('a'):
    print(link.get('data-name'))

# Link to detail page
for product in soup.find_all('a'):
    print(product.get('href'))

# How manay arein stock(0 if Out of Stock)
soup.find_all('div', class_='stock')

# URL of the product image
soup.find_all(name='img')