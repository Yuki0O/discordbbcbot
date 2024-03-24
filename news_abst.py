import aiohttp
from bs4 import BeautifulSoup
import random
import discord
import re
from googletrans import Translator

async def news_abst():
    url = "https://www.bbc.com/news/science-environment-68110310"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            article_soup = BeautifulSoup(res.text(), 'html.parser')
    return article_soup.text

loop = news_abst()