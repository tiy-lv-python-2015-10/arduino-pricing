from pymongo import MongoClient


def search_title(word):
    client = MongoClient()
    db = client.arduino
    cursor = db.products.find({'name': {'$regex': '(?i)' + word}})
    return cursor


def search_price(price):
    client = MongoClient()
    db = client.arduino
    cursor = db.products.find({'price': price})
    return cursor