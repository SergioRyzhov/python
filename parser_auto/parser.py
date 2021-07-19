"""
This is the volkswagen polo-sedan parser for the av.by website.

Why is this car?
I have this car and I want to monitor the prices on a marketplace.
This parser isn't an order, it's the smal project to improve
my python abilities.
"""

import requests
from bs4 import BeautifulSoup
import csv

URL = 'https://cars.av.by/volkswagen/polo-sedan'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
           'accept': '*/*'}
HOST = 'https://cars.av.by'
FILTER = '/filter?brands[0][brand]=1216&brands[0][model]=5920'
FILE = 'cars.csv'


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_digit_from_text(txt):
    temp = []
    for ch in txt:
        if ch.isdigit():
            temp.append(ch)
    return int(''.join(temp))


def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    pagination = soup.find_all('div', class_='paging__button')
    all_items = get_digit_from_text(
        soup.find('div', class_='paging__text').get_text()[-10:])
    items_in_the_page = get_digit_from_text(
        soup.find('div', class_='paging__text').get_text()[:20])
    if pagination:
        return int(all_items / items_in_the_page) + 1


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='listing-item__wrap')

    cars = []
    for item in items:
        car_escape = item.find('div', class_='listing-item__params')\
            .get_text().replace('\u2009', '').replace('\xa0', '')[-8:]
        start_ind = 0
        for ch in car_escape:
            if ch.isalpha():
                start_ind += 1
            else:
                break
        car_escape = car_escape[start_ind:]

        cars.append({
            'title': item.find('h3', class_='listing-item__title').get_text(strip=True),
            'link': HOST + item.find('a', class_='listing-item__link').get('href'),
            'year': item.find('div', class_='listing-item__params').find_next().get_text().replace('\xa0', ''),
            'car_escape': car_escape,
            'usd_price': item.find('div', class_='listing-item__priceusd').get_text()
            .replace('\xa0', '').replace('\u2009', '').replace('≈', ''),
            'byn_price': item.find('div', class_='listing-item__price').get_text()
            .replace('\xa0', '').replace('\u2009', ''),
            'city': item.find('div', class_='listing-item__location').get_text()
        })
    return cars


def save_file(items, path):
    with open(path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Название авто', 'Ссылка', 'Год',
                       'Пробег', '$ цена', 'BYN цена', 'Город'])
        for item in items:
            writer.writerow([item['title'], item['link'], item['year'], item['car_escape'],
                            item['usd_price'], item['byn_price'], item['city']])



def parse():
    html = get_html(URL)
    # print(html.status_code)
    if html.status_code == 200:
        cars = []
        pages_count = get_pages_count(html.text)
        for page in range(1, pages_count + 1):
            print(f'парсинг страницы {page} из { pages_count}...')
            html = get_html(HOST+FILTER, params={'page': page})
            cars.extend(get_content(html.text))
        
        save_file(cars, FILE)
        print(f'получено {len(cars)} автомобилей')
    else:
        print('Error')


parse()
