import aiohttp
from bs4 import BeautifulSoup
import asyncio

async def news_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            article_html = await res.text()
            soup = BeautifulSoup(article_html, 'html.parser')
            elem = soup.find_all("b")
            if elem:   
                return str(elem)
            else:
                return "No body"
async def main():
    article_url = "https://www.bbc.com/news/science-environment-68110310"
    body_search = await news_data(article_url)
    print(body_search)
asyncio.run(main())
