import aiohttp
from bs4 import BeautifulSoup
import random
import discord
import re
from googletrans import Translator


async def news_scrap():
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

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("$news_BBC"):
        loading_msg = await message.channel.send("読み込み中...")
        news = await news_scrap()
        formatted_news = "\n".join(
            [n.replace('[', '').replace(']', '') for n in news])
        loading_msg.delete()
        await message.channel.send(formatted_news)
    elif message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run("TOKEN")
