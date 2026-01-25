# 15.9. Дан текстовый файл. Подсчитать количество символов в нем.

file = open("ggg.txt", encoding="utf-8")
file_r = file.read()
file.close()

answer = len(file_r)
print(answer)
