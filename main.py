import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/')
soup_object = BeautifulSoup(res.text, 'html.parser')
titless = soup_object.select('.titleline')


def show_title(oruko):
    title_list = []
    for index, tile in enumerate(oruko):
        saved_name = oruko[index].getText()
        title_list.append(saved_name)

    return title_list


pprint.pprint(show_title(titless))
