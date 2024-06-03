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
import datetime

import requests
from bs4 import BeautifulSoup

import re


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


class File_log():
    # переменная класса File_log обозначающая имя файла
    name_file = ""

    '''
    функция создающая лог-файл (открывает и закрывает его)
    '''
    def __init__(self, name_file):
        self.name_file = name_file
        function_create = open(name_file, "w")
        function_create.close()


    '''
    функция возвращающая название имени файла
    '''
    def get_name_file(self):
        return self.name_file

    '''
    функция записи в файл
    '''
    def write_text_in_file(self, text):
        is_exist = self.examination_text_is_exist(self, text)
        if is_exist == True:
            print("текст уже есть в файле")
        else:
            write_in_file = open(self.name_file, "a")
            # добавить сюда что-то вроде внести запись информация записывается в такое-то время, такую-то дату
            current_time = datetime.datetime.now().time()
            current_time = str(current_time)
            info = "News added in " + current_time
            write_in_file.write(info + '\n')
            write_in_file.write(text + '\n')
            write_in_file.close()
            print("записала в файл")


    '''
    функция чтения из файла
    '''
    def read_from_file(self):
        f = open(self.name_file, 'r')
        info_in_file = f.read()
        f.close()
        print(info_in_file)
        return info_in_file

    '''
    функция проверки текста уже в файле
    '''
    def examination_text_is_exist(self, text):
        text_in_file = self.read_from_file(self)
        if text in text_in_file:
            return True
        else:
            print("новая информация")
            return False



"""
сделать класс работы с парсингом сайта

функция описывающая характеристики сайта

функция вытягивающая информацию с сайта
"""

class Parsing_of_site():
    text_from_site = ''
#     функция описывающая сам сайт
#     это функция просто прочтения текста с сайта и возвращающая массив из ссылок
    def read_home_internet_page(self):
        url = "https://edition.cnn.com/politics/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # здесь будет запись всех ссылок какие есть на странице
        links = soup.find_all('a')
        array_links = []
        for link in links:
            array_links.append(link.get('href'))
            print(array_links)
        return array_links

            # link = str(link)
            # print(link)
            # pattern = re.compile('href="(.+)"')
            # match = pattern.search(link)
            # print(match)

            # adress = link
            # href = link.get(link)
            # self.read_news_internet_page(self, href)



    # заходим на старницу новую делаем две проверки:
    # есть ли нужные элементы на старнице

    # def examination_needs_element(self, url):
    #     response = requests.get(url)
    #     soup = BeautifulSoup(response.content, 'html.parser')
    #     driver = webdriver.Chrome()
    #     driver.get(url)
    #     try:
    #         element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'p')))
    #         print("Элемент p существует.")
    #     except TimeoutException:
    #         print("Элемент p не существует.")
    #     driver.quit()

    def examination_all_links(self, array):
        for i in array:
            Parsing_of_site.read_news_internet_page(Parsing_of_site, i)


    def read_news_internet_page(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        new_heading = soup.title.text
        new_annotation = soup.p.text
        new_author = soup.find('span', 'byline__name').text
        text_of_news = Text_of_news.__init___(Text_of_news, new_heading, new_annotation, new_author)
        return text_of_news.ready_information(text_of_news)





        # print(soup.title.text)

        # эксперименты:
        # print(soup.span)

        # я беру главную страницу с политикой нахожу там ссылку с нужным ключевым словов,
        # автоматически переходит на страницу пор ссылке и там берет нужные данные
        # берется остнвная страница на ней находится информация по ключевому слову
        # если есть нужные слова переходит на страницу самой нововсти

        # return self.text_from_site
        # print(self.text_from_site)
        keywords = ['Trump']




        print(soup.find_all(text=lambda text: any in keywords))
                            # , 'span', 'container__headline-text'))
        # print(soup.find('span', 'container__headline-text'))




    '''
    функция возвращающая значение текста изъятого с сайта
    '''
    def get_text_from_site(self):
        return self.text_from_site

    '''
    функция устанавливающая новое значение
    '''
    def set_text_from_site(self, new_text):
        self.text_from_site = new_text

    def click_on_link(self):
        pass

    def find_my_text(self, list):
        pass




#     ищу в заголовках, если нахожу нужные упоминания перейти по ссылке открыть страницу и отуда вернуть аннотацию,
# заголовок и автора и записать

'''
Чтобы нажать на ссылку при нахождении нужного текста в Python с использованием Selenium, вам нужно выполнить следующие шаги:
Открыть URL: Сначала откройте целевой URL, где находится нужный текст и ссылка. Это можно сделать с помощью метода driver.get().
Найти элемент: Используйте метод find_element() для поиска элемента, содержащего нужный текст. Например, если это 
текст внутри тега <p>, вы можете использовать следующий код:
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://example.com")

# Находим элемент с нужным текстом
element = driver.find_element(By.XPATH, '//p[contains(text(), "Ваш текст")]')
Проверить наличие ссылки: После нахождения элемента проверьте, есть ли внутри него ссылка. Если да, 
то вы можете нажать на эту ссылку, используя метод click().
# Проверяем, есть ли внутри элемента ссылка
if element.find_element(By.TAG_NAME, 'a'):
 element.find_element(By.TAG_NAME, 'a').click()
Обратите внимание, что этот код предполагает, что внутри элемента с нужным текстом есть только одна ссылка. 
Если ссылок несколько, вам может потребоваться уточнить XPath для точного выбора нужной ссылки.



'''




# функция



"""
класс самой записи в виде словаря имеющая определенные характеристики
заголовок, аннотация, автор 
функция печатать саму запись в удобоваримом формате туСтринг
и уже её переводить и проверять
"""
class Text_of_news():
    heading = ''
    annotation = ''
    author = ''

    """
    функции устанвливающие новые данные заголовка, аннотации статьи, автора
    """
    def __init___(self, heading, annotation, author):
        self.heading = "Heading: " + heading + '\n'
        self.annotation = "Annotation: " + annotation + '\n'
        self.author = "Author: " + author + '\n'
        return self

    def set_heading(self, new_heading):
        self.heading = str("Heading: " + new_heading)

    def set_annotation(self, new_annotation):
        self.annotation = str("Annotation: " + new_annotation)

    def set_author(self, new_author):
        self.author = str("Author: " + new_author)


    """
    функции возвращающие данные заголовка, аннотации статьи, автора
    """
    def get_heading(self):
        return self.heading

    def get_annotation(self):
        return self.annotation
    def get_author(self):
        return self.author

    def ready_information(self):
        text = self.get_heading(self) + self.get_annotation(self) + self.get_author(self)
        return text


'''
функции проверки
'''
def start(name_file):
    File_log.__init__(File_log, name_file)
def working(name_file, text_for_write):
    File_log.get_name_file(File_log)
    File_log.write_text_in_file(File_log, text_for_write)
    File_log.read_from_file(File_log)
#
#


# Parsing_of_site.read_internet_page(Parsing_of_site)
# url = 'https://edition.cnn.com/2024/05/30/politics/bob-menendez-trial-nadine-texts/index.html'
# text_for_write = Parsing_of_site.read_news_internet_page(Parsing_of_site, url)
# name_file = "CNN.txt"
# start(name_file)
# working(name_file, text_for_write)
# working(name_file, text_for_write)
array_site = Parsing_of_site.read_home_internet_page(Parsing_of_site)
Parsing_of_site.read_news_internet_page(Parsing_of_site, array_site)

