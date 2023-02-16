import requests
from bs4 import BeautifulSoup as b


class Post(object):
    url: str
    title: str
    img: str

    def __init__(self, url, title, img):
        self.url = url
        self.title = title
        self.img = img


def news_parser(url: str):
    post_list: list[Post] = []

    req = requests.get(url)
    soup = b(req.text, 'html.parser')
    find_block_news = soup.find_all('a', class_='item')
    for elem in find_block_news:
        post_list.append(
            Post(
                url=elem['href'],
                title=elem.find('div', class_="title").text,
                img=elem.find('div', class_="img-block")
            )
        )
    return post_list
