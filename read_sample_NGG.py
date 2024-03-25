import random
import asyncio
import aiohttp
from bs4 import BeautifulSoup


async def news_scrap_NGG() -> list[str]:
    url = "https://natgeo.nikkeibp.co.jp/nng/news/genre_science.shtml"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            soup = BeautifulSoup(await res.text(), 'html.parser')
    article_links = soup.find_all(
        class_=["firstPageFirstItem FREE",
                "firstPageBorderItem ", "FREE"],
        limit=11)
    tops = "https://natgeo.nikkeibp.co.jp/"
    titles_urls = []
    random_num = random.randint(0, 9)
    choiced_article = article_links[random_num]
    article_soup = BeautifulSoup(str(choiced_article), 'html.parser')
    article_title = article_soup.find('h3').get_text()
    article_absts = article_soup.find('p').get_text()
    article_url = tops + article_soup.find('a')['href']
    # article_url = tops + article_soup.find(href=re.compile("atcl")).get_text()
    titles_urls.append(f'『{article_title}』\n{article_absts}\n{article_url}')
    return titles_urls


async def main():
    prt = await news_scrap_NGG()
    formatted_news = "\n".join(
        [n.replace('[', '').replace(']', '') for n in prt])
    print(formatted_news)
asyncio.run(main())
