import random
import re
import asyncio
import aiohttp
from bs4 import BeautifulSoup

async def news_scrap_JST() -> list[str]:
    url = "https://scienceportal.jst.go.jp/newsflash/"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            soup = BeautifulSoup(await res.text(), 'html.parser')
    article_links = soup.find_all(href=re.compile(
        "index"), limit=11)
    tops = "https://scienceportal.jst.go.jp/newsflash/"
    titles_urls = []
    random_num = random.randint(1, 10)
    choiced_article = article_links[random_num]
    #html_title = choiced_article.contents[0]
    title_soup = BeautifulSoup(str(choiced_article), 'html.parser')
    article_title = title_soup.find("h3")
    article_url = tops + choiced_article.attrs['href']
    titles_urls.append(f'{article_title},\n{article_url}')
    return titles_urls

async def main():
    prt = await news_scrap_JST()
    print(prt)
asyncio.run(main())