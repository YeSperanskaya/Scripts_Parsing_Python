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




класс самой записи в виде словаря имеющая определенные характеристики
заголовок, аннотация, автор 
функция печатать саму запись в удобоваримом формате туСтринг
и уже её переводить и проверять
"""



'''
функции проверки
'''
def start(name_file):
    File_log.__init__(File_log, name_file)
def working(name_file):
    File_log.get_name_file(File_log)
    File_log.write_text_in_file(File_log, "gfdgdgdfgdfgdfg")
    File_log.read_from_file(File_log)


name_file = "CNN.txt"
start(name_file)
working(name_file)
working(name_file)
