import requests
from bs4 import BeautifulSoup
import os

my_headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'}
try:
    os.mkdir('book_images')
except FileExistsError:
    pass

with open('books.txt','r',encoding='utf-8') as file:
    links_text=file.read()
    links_list=links_text.split('\n')

for i ,book in enumerate(links_list):
    with open (f'data/book_images/{i}.jpg','wb') as file:
        file.write(requests.get(book,headers=my_headers).content)