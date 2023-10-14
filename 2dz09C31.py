def change_file(filename1): # С помощью change_file принимаем имя файла в качестве аргумента
    with open('resultat_file', 'w', encoding='utf-8') as new_file, open(filename1, 'r', encoding='utf-8') as parent_file: # Открываем файл 'resultat_file' для записи модифицированных данных,
# и файл 'filename1' для чтения исходных данных
        for i in parent_file: # Перебор каждой строки в файле, который открыт
            n_spisok = i.strip().split() # Разделение текущей строки на слова и удаление начальных и конечных пробелов
print(n_spisok) # Вывод текущей строки как список слов
    for j, x in enumerate(n_spisok): # Перебор каждого слова в списке
         if len(x) >= 3: # Если длина слова больше или равна 3 символам
n_spisok[j] = f'{x[0]}{x[0]}{x[2].upper()}{x[3:]}' # Процесс модификации слова
new_file.write(' '.join(n_spisok)) # Запись модифицированного слова обратно в файл 'resultat_file', разделение их пробелами
change_file('52.txt') # Вызов функции change_file, передача имени файла '52.txt' для изменения
