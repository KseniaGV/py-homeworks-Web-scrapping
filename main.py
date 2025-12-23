import requests
import bs4

## Определяем список ключевых слов:
KEYWORDS = ['дизайн', 'фото', 'web', 'python']

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept-Language': 'ru-RU,ru;q=0.9'
}

response = requests.get('https://habr.com/ru/articles/', headers=headers)
soup = bs4.BeautifulSoup(response.text, features='lxml')

articles_block = soup.find_all('article', class_='tm-articles-list__item')
print(f"Найдено статей: {len(articles_block)}")

for article in articles_block:
    #ищем ссылку
    link = 'https://habr.com' + article.select_one('a.tm-title__link')['href']

    #ищем название статьи
    title = article.find('a', class_ = 'tm-title__link').text.strip().lower()

    #ищем дату статьи
    time = article.select_one('time')['title']

    #ищем текст статьи
    article_text = article.find('div', class_='article-formatted-body').text.lower()
    if not article_text:
        article_text = article.find('div', class_='tm-article-body').text.lower()

    if any(keyword in article_text or keyword in title for keyword in KEYWORDS):
        print(f'{time} - {title} - {link}')






