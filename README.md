# Arduino Sales

## Description
Unfortunately, there are many sources of data that are not readily available via an api.  In these situations you can use a scraper
to get the same information just in a bit more manual way.  In this assignment you will be scraping a site and storing the information
in your own local database.

## Learning Objectives
* Using an HTML scrapper to get data
* Storing the data into a NoSQL database

## Details

### Requirements
* Pull Request
* README.md changed to include how to run the software

### Normal Mode
We want to store the product data for arduinos being sold on AdaFruit's website.  They are a great source for these types of devices
but unfortunately they don't have a readily available api to use to get this information.  Using beautifulsoup4 scrape the listing page
https://www.adafruit.com/category/17 

* Use beautiful soup to scrape the following page (https://www.adafruit.com/category/17)
* For each product get the following:
	* Product Id
	* Price
	* Name
	* Link to detail page
	* How many are in stock (0 if Out of Stock)
	* URL of the product image
* Store this information in mongodb where the _id of the product in mongo is the product id of the site
* Create the following functions:
	* Search for a specific price and return all documents
	* Search for products with a given word in their title

### Hard Mode
* For each product use the detail page link to retrieve and parse the detail page
* Parse and store the following:
	* Any quantity discounts
	* Any technical detail bullet points
