from bs4 import BeautifulSoup
import requests

stock_page = 'http://www.lse.co.uk/ShareChat.asp?ShareTicker='
ticker = input("Ticker? ")

page = requests.get(stock_page + ticker)
html = page.text

soup = BeautifulSoup(html, 'html.parser')

complete_posts = []

post_titles = []
posts = []
post_dates = []

current_price = soup.find('table', attrs={'class': 'SharePriceInfoHeader'}).text

for i in range(1, 24):
    post_title = soup.find_all('div', attrs={'class': 'FullChatSubject'})[i].text
    post = soup.find_all('div', attrs={'class': 'FullChatText'})[i].text
    date = soup.find_all('div', attrs={'class': 'FullChatDate'})[i].text
    post_titles.append(post_title)
    posts.append(post)
    post_dates.append(date)

def get_current_price():
    return current_price

def get_post_titles():
    return post_titles

def get_posts():
    return posts

def get_post_dates():
    return post_dates

def get_ticker():
    return ticker

