import requests
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd

data = []

for p in range(1, 6):
    print(p)
    kinopoisk_url = f"https://www.kinopoisk.ru/lists/movies/top250/?page={p}"

    r = requests.get(kinopoisk_url)
    sleep(10)

    soup = BeautifulSoup(r.text, 'lxml')

    films = soup.findAll('div', class_="styles_root__ti07r")


    for film in films:
        try:
            link = "https://www.kinopoisk.ru"+film.find('a', class_="base-movie-main-info_link__YwtP1").get('href')
            ru_name = film.find('a', class_="base-movie-main-info_link__YwtP1").find('span', class_ = "styles_mainTitle__IFQyZ styles_activeMovieTittle__kJdJj").text
            orig_name = film.find('a', class_="base-movie-main-info_link__YwtP1").find('span', class_="desktop-list-main-info_secondaryText__M_aus").text
            info_about_1 = film.find('a', class_="base-movie-main-info_link__YwtP1").find('span', class_="desktop-list-main-info_truncatedText__IMQRP").text
            info_about_2 = film.find('a', class_="base-movie-main-info_link__YwtP1").findAll('span', class_="desktop-list-main-info_truncatedText__IMQRP")[1].text
            rate = film.find('span', class_="styles_kinopoiskValuePositive__vOb2E styles_kinopoiskValue__9qXjg").text
            page = film.find('a', class_="styles_page__zbGy7 styles_active__fPiyK").text

            print("page =", page)
            data.append([link, ru_name, orig_name, info_about_1, info_about_2, rate, page])

        except:
            link = ru_name = orig_name = info_about_1 = info_about_2 = rate = page = 'Unknown'
    print(len(data))


header = ['link', 'ru_name', 'orig_name', 'info_about_1', 'info_about_2', 'rate', 'page']

df = pd.DataFrame(data, columns=header)
df.to_excel('C:/Users/NerdY/Desktop/table/kinopoisk_data.xlsx')