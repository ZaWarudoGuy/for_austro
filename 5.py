with open('astronaut_time.txt', encoding='utf8') as f:
    """открываем и записываем файл. Неизвестно из условия что. В начале написано что используем именно astronaut_time.txt"""
    reader = f.readlines()[1:]
    pure_data = []
    for i in reader:
        pure_data.append(i.strip().split('>'))


"""создаем саму хэш таблицу где ключу соотвествует остальные значения каюты"""
hash_table = dict()
for row in pure_data:
    hash_table[row[2]] = [row[0], row[1], row[3], row[4]]

count = 0
"""реализация вывода"""
for key in hash_table:
    if count == 10:
        break
    """выводим данные: "ключ: значение" """
    print(key, hash_table[key])
    count += 1
