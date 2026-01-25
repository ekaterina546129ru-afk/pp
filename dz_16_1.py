#  Создать текстовый файл и записать в него фразу Здравствуй, мир!.

file = open('hello.txt', 'a+', encoding='utf-8')

file_write = file.write('Здравствуй, мир!')

file.close()

