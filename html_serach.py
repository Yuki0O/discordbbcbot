import aiohttp
from bs4 import BeautifulSoup
import asyncio
import re

async def news_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            article_html = await res.text()
            soup = BeautifulSoup(article_html, 'html.parser')
            elem = soup.find_all(href=re.compile("index"), limit=10)
            if elem:   
                return str(elem)
            else:
                return "No body"
async def main():
    site_url = "https://scienceportal.jst.go.jp/newsflash/"
    tag_search = await news_data(site_url)
    print(tag_search)
asyncio.run(main())
