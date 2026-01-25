# 15.8. Дан текстовый файл. Подсчитать количество строк в нем.

file = open("hhh.txt", "r", encoding="utf-8")
file_r = file.read()
file.close()

stroka_count = len(file_r.splitlines())

print(f"Количество сток в тексте: {stroka_count}")
