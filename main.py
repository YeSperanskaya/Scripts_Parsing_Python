"""
Используя любой скриптовый язык (напр Python, Ruby, Javascript, Perl) написать скрипт, извлекающий новости
(отдельно заголовок, анотацию, авторов) из веб-страницы новостного агенства, но не используя RSS.
Требуется написать такой скрипт, который будучи запущен на на определенное время (например 4 часа) автоматически
выделит и отобразит/запишет в лог все статьи, которые будут опубликованы за этот период (т.е. только новые),
при этом выводить нужно новости содержащие упоминания Республиканской и Демократической партий США.

Работа сдается в виде:
1) одиночного файла скрипта, готового для запуска
2) указание на зависимые библиотеки (если есть)
3) скриншот и лог работы скрипта на протяжении 4 часов с выводом всех найденых новостей
(если за 4 часа не нашлось - выбирайте другое новостное агенство)
Возможно предоставление решения в виде публичной песочницы, например на https://repl.it
"""

# полезные ссылки
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# https://docs-python.ru/packages/modul-user-agents-python/
# https://habr.com/ru/companies/selectel/articles/754674/
# https://skillbox.ru/media/code/parsing-sayta-vmeste-s-python-i-bibliotekoy-beautiful-soup-prostaya-instruktsiya-v-tri-shaga/

# импортируем модуль
# import requests
# from bs4 import BeautifulSoup
#
# st_accept = "text/html" # говорим веб-серверу,
#                         # что хотим получить html
# # имитируем подключение через браузер Mozilla на macOS
# st_useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"
# # формируем хеш заголовков
# headers = {
#    "Accept": st_accept,
#    "User-Agent": st_useragent
# }
#
# t = True
# a = 0
# while (t == True):
#    # отправляем запрос с заголовками по нужному адресу
#    req = requests.get("https://edition.cnn.com/", headers)
#    # считываем текст HTML-документа
#    src = req.text
#    #print(src)
#
#
#    # инициализируем html-код страницы
#    soup = BeautifulSoup(src, 'lxml')
#    # считываем заголовок страницы
#    title = soup.title.string
#    if "void" in soup:
#       print(title)
#    a += 1
#    if a == 25:
#       t = False
#    # else:
#    #    print("не нашел")
#    # Программа выведет: Курсы - Блог компании Селектел
#
#    # надо устанавливать определнное время запуска
#    # нудо устанавливать поисковик
#    # надо установить запись в файл


import requests
import json
from bs4 import BeautifulSoup

# URL веб-страницы новостного агентства


def get_news():
    url = 'https://www.independent.co.uk/topic/republicans/'
    headers = {'User-Agent': 'Mozilla/5.0'}
    # Отправка запроса к веб-странице
    response = requests.get(url, headers=headers, allow_redirects=True)
    # Анализ HTML-кода страницы
    soup = BeautifulSoup(response.content, 'html.parser', from_encoding='Windows-1251')

    # Извлечение заголовков статей
    headlines = soup.title.string
    #print(headlines)

    # Извлечение аннотаций статей
    annotations = soup.find_all('p')

    # Извлечение авторов статей
    authors = soup.find_all('a')

# Фильтрация статей по содержанию
    filtered_articles = []
    for headline, annotation, author in zip(headlines, annotations, authors):
        #if 'republican' in headline.text or 'democratic' in headline.text:
        if 'Jersey' in headline.text:
            filtered_articles.append({
                'title': headline.text,
                'annotation': annotation.text,
                'author': author.text
            })
    return filtered_articles

# проверка наличия текста в лог-файле
# def text_in_file(text, file):
#     if text in file:
#         return True
#     else:
#         False

# функция, которая записывает данные с сайта
def log_in_file(text):
    # открываем файл для проверки
    with open('example.txt', 'r') as file:
        content = file.read()
        # # Преобразуем словарь в строку
        string_text = json.dumps(text)
        # for i in text:
        #     text[i] = str(text[i])
        # превращаю list в строку
        #str_text = ', '.join(text)
    if string_text in content:
        file.close()
    else:
    # Открываем файл для записи
        with open('example.txt', 'a') as file:
        # Записываем текст в файл
            file.write(string_text + '\n')
        # Закрываем файл
            file.close()

res = True
count = 0

# Создаем новый файл
with open('example.txt', 'w') as file:
    file.close()

while (res == True):
    log_in_file(get_news())
    count += 1
    if count == 2:
        res = False




# if __name__ == 'USA':
#     print(get_news())

