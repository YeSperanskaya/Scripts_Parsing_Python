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

    # функция создающая лог-файл (открывает и закрывает его)
    def __init__(self, name_file):
        self.name_file = name_file
        function_create = open(name_file, "x")
        function_create.close()

    '''
    функция возвращающая название имени файла
    '''
    def get_name_file(self):
        return self.name_file



    def write_text_in_file(self, text):
        self.name_file = open(self, "a")
        self.name_file.write(text + '\n')
        self.name_file.close()
        return self.name_file



def start():
    name_file = "CNN"
    my_file = File_log.__init__(File_log, "CNN.txt")
    File_log.write_text_in_file(my_file, "rsdrfsfsefsefsef")

start()
