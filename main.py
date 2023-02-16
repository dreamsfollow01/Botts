from pars import news_parser
from aiogram.utils.markdown import link


URL = 'https://www.autocentre.ua/avtosport'

news_list = {"news": news_parser(URL)[0].title,
             "url": news_parser(URL)[0].url,
             "img": news_parser(URL)[0].img}

message_form = f"news: {news_parser(URL)[0].title}\n{link('tst', news_parser(URL)[0].url)}"
