from skpy import Skype
from bs4 import BeautifulSoup
import requests
import responses

import stock_chat
import data

username = #YOUR_USERNAME_HERE
password = #YOUR_PASSWORD_HERE

sk = Skype(username, password)

contact = #YOUR SKYPE CONTACT TO RECIEVE DATA (example "live:skypeuser")

ch = sk.contacts[contact].chat

post_titles = stock_chat.get_post_titles()
posts = stock_chat.get_posts()
post_dates = stock_chat.get_post_dates()

current_price = stock_chat.get_current_price()

ch.sendMsg("_____________________________________________________")
ch.sendMsg(stock_chat.get_ticker())
ch.sendMsg(current_price)
for post_title, post, date in zip(post_titles, posts, post_dates):
    ch.sendMsg(post_title)
    ch.sendMsg(date)
    ch.sendMsg(post)
