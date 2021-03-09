from bs4 import BeautifulSoup
import requests
import numpy


response = requests.get("https://news.ycombinator.com/")
yc_response = response.text

soup = BeautifulSoup(yc_response, "html.parser")
print(soup.title)

articles = soup.findAll(name="a", class_="storylink")

article_texts = []
article_links = []

for article in articles:
    text = article.getText()
    link = article.get("href")

    article_texts.append(text)
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]


text = numpy.array(article_texts)
links = numpy.array(article_links)
upvotes = numpy.array(article_upvotes)
indx = upvotes.argsort()
print(f"{text[indx]}\n{links[indx]}\n{upvotes[indx]}")
