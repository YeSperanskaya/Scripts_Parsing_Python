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
import time

from pip._internal.utils import datetime

# URL веб-страницы новостного агентства

'''
Эта функция содержит в себе адрес ссылки, проверяет ее на наличие ключевого слова и возвращает словарь
'''
def get_news():
    url = 'https://edition.cnn.com/'
    headers = {'User-Agent': 'Mozilla/5.0'}
    # Отправка запроса к веб-странице
    response = requests.get(url, headers=headers, allow_redirects=True)
    # Анализ HTML-кода страницы
    soup = BeautifulSoup(response.content, 'html.parser', from_encoding='utf-8')

    # Извлечение заголовков статей
    headlines = soup.find_all('span')
    print(headlines)

    # Извлечение аннотаций статей
    annotations = soup.find_all('p')

    # Извлечение авторов статей
    authors = soup.find_all('a')

# Фильтрация статей по содержанию
    filtered_articles = []
    for headline, annotation, author in zip(headlines, annotations, authors):
        #if 'republican' in headline.text or 'democratic' in headline.text:
        #if 'CNN' in annotation.text or 'republ' in annotation.text:
        if 'democr' in annotation.text or 'republ' in annotation.text or 'democr' in headline.text or 'republ' in headline.text:
            filtered_articles.append({
                'title': headline.text,
                'annotation': annotation.text,
                'author': author.text
            })
    print("прошла функция get_news()")
    return filtered_articles


# #функция, которая создает новое название для файла
# def create_file(file_name):
#     cur_time = datetime.datetime.now()
#     filename_full = file_name + "_" + cur_time.strftime(
#         '%Y-%m-%d_%H-%M-%S')
#     fd = open(filename_full, 'w', encoding='utf-8')
#     fd.write(
#         f"{cur_time.strftime('%Y-%m-%d %H:%M:%S')}: Script started\n")
#     fd.close()


# функция, которая записывает данные с сайта
def log_in_file(text):
    # открываем файл для проверки
    with open('example.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        # Преобразую словарь в строку
        str_in_file = json.dumps(content)
        print(str_in_file)
        str_in_text = json.dumps(text)
        print(str_in_text)

    # превращаю list в строку
        if str_in_text in str_in_file:
            print("похожий текст найден")
            file.close()
        else:
            file.close()
        # Открываем файл для записи
            with open('example.txt', 'a', encoding='utf-8') as file:
            # Записываем текст в файл
                file.write(str_in_text)
            # Закрываем файл
                file.close()
                print("текст успешно записан")




# Создаю новый файл
with open('example.txt', 'w', encoding='utf-8') as file:
    file.close()

res = True
delay_time = 600
count = 0
while (res == True):
    log_in_file(get_news())
    count += 1
    if count == 240:
        res = False
    else:
        time.sleep(delay_time)



