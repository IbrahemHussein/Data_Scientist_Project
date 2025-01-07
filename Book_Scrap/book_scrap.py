import requests
from bs4 import BeautifulSoup
url='https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
response=requests.get(url)
response.encoding='utf-8'
soup=BeautifulSoup(response.text,features='html.parser')

# name

name=soup.find('div',class_='product_main').h1.text
print(name)

#price
price=float(soup.find('p',class_='price_color').text[1:])
print(price)
# instock availability
instock=int(soup.find('p',class_='instock availability').text.strip().split('(')[1].split(' ')[0])
print(instock)

#star-rating Three
number_dict={'One':1,'Tow':2,'Three':3,'Four':4,'Five':5}
star_rating=soup.find('p',class_='star-rating')
rating_string=star_rating['class'][1]
rating=number_dict[rating_string]
print(rating)

# catalogue
catalogue=soup.find('ul','breadcrumb').find_all('a')[-1].text
print(catalogue)

# Description
description=soup.find('div',class_='sub-header').find_next_siblings()[0].text
print(description)

#UPC

upc=soup.find('th',string='UPC').find_next_siblings()[0].text
print(upc)

#img

img_url=soup.find('div',class_='item active').img['src'][6:]
print(img_url)