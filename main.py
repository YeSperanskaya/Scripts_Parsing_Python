'''
Используя любой скриптовый язык (напр Python, Ruby, Javascript, Perl) написать скрипт, извлекающий новости
(отдельно заголовок, анотацию, авторов) из веб-страницы новостного агенства, но не используя RSS. Требуется
написать такой скрипт, который будучи запущен на на определенное время (например 4 часа) автоматически выделит
и отобразит/запишет в лог все статьи, которые будут опубликованы за этот период (т.е. только новые), при этом
выводить нужно новости содержащие упоминания Республиканской и Демократической партий США.
'''
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
        write_in_file = open(self.name_file, "a")
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
        text_in_file = self.read_from_file()
        if text in text_in_file:
            print("текст уже есть в файле")
            return True




def start(name_file):
    File_log.__init__(File_log, name_file)
def working(name_file):
    File_log.get_name_file(File_log)
    File_log.write_text_in_file(File_log, "gfdgdgdfgdfgdfg")
    File_log.read_from_file(File_log)


name_file = "CNN.txt"
start(name_file)
working(name_file)
