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
# найти лог-файл
# функция чтения лог-файла
# black и white листы

# 4 признака и сравнивать
#
#

# импортируем модуль
import requests
from bs4 import BeautifulSoup

st_accept = "text/html" # говорим веб-серверу,
                        # что хотим получить html
# имитируем подключение через браузер Mozilla на macOS
st_useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"
# формируем хеш заголовков
headers = {
   "Accept": st_accept,
   "User-Agent": st_useragent
}

# отправляем запрос с заголовками по нужному адресу
req = requests.get("https://selectel.ru/blog/courses/", headers)
# считываем текст HTML-документа
src = req.text
print(src)


# инициализируем html-код страницы
soup = BeautifulSoup(src, 'lxml')
# считываем заголовок страницы
title = soup.title.string
print(title)
# Программа выведет: Курсы - Блог компании Селектел

"""
from selenium import webdriver as wd
from bs4 import BeautifulSoup

browser = wd.Chrome("/usr/bin/chromedriver/")

# регистрируем кнопку "Поиск" и имитируем нажатие
open_search = browser.find_element_by_class_name("header_search")
open_search.click()
# регистрируем текстовое поле и имитируем ввод строки "Git"
search = browser.find_element_by_class_name("search-modal_input")
search.send_keys("Git")



# ставим на паузу, чтобы страница прогрузилась
time.sleep(3)
# загружаем страницу и извлекаем ссылки через атрибут rel
soup = BeautifulSoup(browser.page_source, 'lxml')
all_publications = \
   soup.find_all('a', {'rel': 'noreferrer noopener'})[1:5]
# форматируем результат
for article in all_publications:
   print(article['href'])
"""

