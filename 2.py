import csv


def vstav_sort(arr):
    """сортировка вставками, сортируем вместе с словами так как номер кабины не только число, считаем все значения в общее число"""
    """
    Описание функции:
    функция сортирует заданный список по ключу за o(n** 2).
    
    Описание аргументов:
    arr - сам список который сортируем, его по итогу и возвращаем.
    
    
    """
    for i in range(len(arr)):
        for j in range(i, 0, -1):
            if arr[j][1] < arr[j-1][1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr


with open('new_time.csv', encoding='utf8') as f:
    """открываем и сортируем файл"""
    reader = list(csv.reader(f, delimiter=','))[1:]
    reader = vstav_sort(reader)

    """выводим первые 3"""
    for i in range(3):
        print(f'На станции {reader[i][1]} в каюте {reader[i][2]} восстановлено время. Актуальное время: {reader[i][-1]}')