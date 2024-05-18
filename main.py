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
req = requests.get("https://www.google.com/search?gs_ssp=eJzj4tVP1zc0LEq3tCg0zq5QYDRgdGDw4kpPTc1OKkrMzCsGAIbWCRE&q=geekbrains&oq=&gs_lcrp=EgZjaHJvbWUqDwgCEC4YJxjHARjqAhjRAzIPCAAQLhgnGMcBGOoCGNEDMgkIARAjGCcY6gIyDwgCEC4YJxjHARjqAhjRAzIJCAMQIxgnGOoCMgkIBBAjGCcY6gIyCQgFECMYJxjqAjIJCAYQIxgnGOoCMgkIBxAjGCcY6gLSAQkxNTE3ajBqMTWoAgiwAgE&sourceid=chrome&ie=UTF-8", headers)
# считываем текст HTML-документа
src = req.text
#print(src)


# инициализируем html-код страницы
soup = BeautifulSoup(src, 'lxml')
# считываем заголовок страницы
title = soup.title.string
print(title)
# Программа выведет: Курсы - Блог компании Селектел



