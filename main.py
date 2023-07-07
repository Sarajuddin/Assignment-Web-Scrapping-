import requests
from bs4 import BeautifulSoup
import csv

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def fetch_and_save_data():
    product_urls = []
    product_names = []
    product_prices = []
    product_ratings = []
    no_of_reviews = []
    
    for i in range(1, 21):
        url = f"https://www.amazon.in/s?k=bags&page={i}&ref=sr_pg_2"

        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.content, 'html.parser')
        # print(soup.prettify())

        products = soup.select("div.a-section.a-spacing-small.a-spacing-top-small")
        # print(products)
        
        for product in products:
            if product.find("a") is not None:
                if not product.find("a").get('href').startswith("http"):
                    
                    product_urls.append(product.find("a").get('href'))
                    # print(product.find("a").get('href'))
                    
                    product_names.append(product.find("span", class_="a-size-medium").get_text())
                    # print(product.find("span", class_="a-size-medium").get_text())
                    
                    product_prices.append(product.find("span", class_="a-offscreen").get_text())
                    # print(product.find("span", class_="a-offscreen").get_text())
                    
                    product_ratings.append(product.find("span", class_="a-icon-alt").get_text())
                    # print(product.find("span", class_="a-icon-alt").get_text())

                    no_of_reviews.append(product.find("span", class_="a-size-base").get_text())
                    # print(product.find("span", class_="a-size-base").get_text())
        
    # print(product_urls)
    # print(product_names)
    # print(product_prices)
    # print(product_ratings)
    # print(no_of_reviews)

    fields = ['Product URL', 'Product Name', 'Product Price', 'Rating', 'Reviews'] 
    with open("data.csv", "w", encoding='utf-8', newline='') as file:
        csvObj = csv.writer(file)
        csvObj.writerow(fields)
        
        for tup in zip(product_urls, product_names, product_prices, product_ratings, no_of_reviews):
            print(list(tup))
            csvObj.writerow(list(tup))


fetch_and_save_data()