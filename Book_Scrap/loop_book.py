import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl


url='https://books.toscrape.com/'
my_headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'}
response=requests.get(url,headers=my_headers)
response.encoding='utf-8'
soup=BeautifulSoup(response.text,features='html.parser')

books_dict={
    'name':[],
    'price':[],
    'instock':[],
    'rating':[],
    'catalogue':[],
    'description':[],
    'upc':[],
    'img_url':[]
}
number_dict={'One':1,'Two':2,'Three':3,'Four':4,'Five':5}


current_page=int(soup.find('li',class_='current').text.strip().split(' ')[-1])
print(current_page)
for page in range(1,current_page+1):
    print(f'page====>{page}')
    url=f'https://books.toscrape.com/catalogue/page-{page}.html'
    response=requests.get(url,headers=my_headers)
    response.encoding='utf-8'
    soup=BeautifulSoup(response.text,features='html.parser')
    books=soup.find_all('article',class_='product_pod')
    for book in books:
        book_url='https://books.toscrape.com/catalogue/' + book.h3.a['href']
        book_response=requests.get(book_url,headers=my_headers)
        book_response.encoding='utf-8'
        book_soup=BeautifulSoup(book_response.text,features='html.parser')
        
        name=book_soup.find('div',class_='product_main').h1.text
        books_dict['name'].append(name)

        price=float(book_soup.find('p',class_='price_color').text[1:])
        books_dict['price'].append(price)

        instock=int(book_soup.find('p',class_='instock availability').text.strip().split('(')[1].split(' ')[0])
        books_dict['instock'].append(instock)

        star_rating=book_soup.find('p',class_='star-rating')
        rating_string=star_rating['class'][1]
        rating=number_dict[rating_string]
        books_dict['rating'].append(rating)
        catalogue=book_soup.find('ul','breadcrumb').find_all('a')[-1].text
        books_dict['catalogue'].append(catalogue)
        try:
            description=book_soup.find('div',class_='sub-header').find_next_siblings()[0].text
            books_dict['description'].append(description)
        except:
            books_dict['description'].append('description not found')

        upc=book_soup.find('th',string='UPC').find_next_siblings()[0].text
        books_dict['upc'].append(upc)
        img_url='https://books.toscrape.com/' + book_soup.find('div',class_='item active').img['src'][6:]
        books_dict['img_url'].append(img_url)
        with open('data/books.txt','a',encoding='utf-8') as file:
            file.write(img_url + '\n')


df=pd.DataFrame(books_dict)
df.to_excel('data/books.xlsx')