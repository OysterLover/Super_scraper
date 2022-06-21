import bs4
import requests
from fake_headers import Headers
from bs4 import BeautifulSoup
import re

if __name__ == "__main__":
    KEYWORDS = {'1С', 'JavaScript', 'GitHub', 'Python'}

    header = Headers(
        browser="chrome",  # Generate only Chrome UA
        os="win",  # Generate ony Windows platform
        headers=True  # generate misc headers
    )

    base_url = 'https://habr.com'
    url = base_url + '/ru/all/'
    res = requests.get(url, headers=header.generate())
    text = res.text
    # print(text)
    soup = bs4.BeautifulSoup(text, features='html.parser')
    articles = soup.find_all('article')
    for article in articles:
        posts = article.find_all('p')
        for element in posts:
            text = set(re.findall('[a-zа-яё]+', element.text, flags=re.IGNORECASE))
            if KEYWORDS.intersection(text):
                data = article.find('time')
                title = article.find('h2').find('span')
                link = article.find(class_='tm-article-snippet__title-link').attrs['href']
                print(f'''{data.text} - "{title.text}" - {base_url}{link}''')
            else:
                pass



