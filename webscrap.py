import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r = requests.get(url)
print(r.status_code)

soup = BeautifulSoup(r.text,"lxml")
product_name = []
names = soup.find_all("a",class_ = "title")
for i in names:
    name = i.text
    product_name.append(name)
print(product_name)

prices = []
prices_list = soup.find_all("h4",class_ = "price float-end card-title pull-right")
for i in prices_list:
    price = i.text
    prices.append(price)
print(prices)

description = []
des = soup.find_all("p",class_ = "description card-text")
for i in des:
    desc = i.text
    description.append(desc)
print(description)

df = pd.DataFrame({"product_name": product_name, "prices":prices, "description":description})
print(df)

df.to_csv("product_details.csv")

