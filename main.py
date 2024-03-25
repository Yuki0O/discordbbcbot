import random
import re

import aiohttp
import discord
from bs4 import BeautifulSoup
from googletrans import Translator

from discordbbcbot.settings import ApplicationSettingsHandler


async def news_scrap_BBC() -> list[str]:
    url = "https://www.bbc.com/news/science_and_environment"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            soup = BeautifulSoup(await res.text(), 'html.parser')
    article_links = soup.find_all(href=re.compile(
        "/news/science-environment"), limit=10)
    BBC = "https://www.bbc.com"
    titles_urls = []
    random_num = random.randint(0, 9)
    choiced_article = article_links[random_num]
    html_title = choiced_article.contents[0]
    title_soup = BeautifulSoup(str(html_title), 'html.parser')
    article_title = title_soup.get_text()
    article_url = BBC + choiced_article.attrs['href']
    translator = Translator()
    translated = translator.translate(article_title, dest="ja").text
    titles_urls.append(f'{article_title},\n{translated},\n{article_url}')
    return titles_urls

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
    title_soup = BeautifulSoup(str(choiced_article), 'html.parser')
    article_title = title_soup.find("h3").get_text()
    article_url = tops + choiced_article.attrs['href']
    titles_urls.append(f'{article_title},\n{article_url}')
    return titles_urls

async def news_scrap_NGG() -> list[str]:
    url = "https://natgeo.nikkeibp.co.jp/nng/news/genre_science.shtml"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            soup = BeautifulSoup(await res.text(), 'html.parser')
    article_links = soup.find_all(
        class_=["firstPageFirstItem FREE",
                "firstPageBorderItem ",
                "FREE"], limit=11)
    tops = "https://natgeo.nikkeibp.co.jp/"
    titles_urls = []
    random_num = random.randint(0, 9)
    choiced_article = article_links[random_num]
    article_soup = BeautifulSoup(str(choiced_article), 'html.parser')
    article_title = article_soup.find('h3').get_text()
    article_absts = article_soup.find('p').get_text()
    article_url = tops + article_soup.find('a')['href']
    titles_urls.append(f'『{article_title}』\n{article_absts}\n{article_url}')
    return titles_urls

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready() -> None:
    print(f'We have logged in as {client.user}')


@client.event
async def news_send(source: str, message: discord.Message):
    loading_msg = await message.channel.send("読込中")
    if source == "BBC":
        news = await news_scrap_BBC()
    elif source == "JST":
        news = await news_scrap_JST()
    elif source == "NGG":
        news = await news_scrap_NGG()
    formatted_news = "\n".join(
            [n.replace('[', '').replace(']', '') for n in news])
    await loading_msg.delete()
    await message.channel.send(formatted_news)


@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return
    if message.content.startswith("$news_BBC"):
        await news_send("BBC",message)
    if message.content.startswith("$news_JST"):
        await news_send("JST",message)
    if message.content.startswith("$news_NGG"):
        await news_send("NGG",message)
    if message.content.startswith("$news_RAND"):
        random_source = random.choice(["BBC","JST","NGG"])
        await news_send(random_source,message)
    elif message.content.startswith('$hello'):
        await message.channel.send('Hello!')


if __name__ == "__main__":
    settings_handler = ApplicationSettingsHandler()
    settings = settings_handler.load()

    client.run(settings.discord_token)
