import csv


with open('new_time.csv', encoding='utf8') as f:
    """открываем и записываем файл"""
    reader = list(csv.reader(f, delimiter=','))[1:]


"""создаем списки в которых храним данные об остановках"""
fir_part_day = []
sec_part_day = []

for i in reader:
    """задаем и определяем по времни кому в какой список попасть"""
    cur_hour, cur_min, cur_sec = list(map(int, i[-2].split(':')))
    if cur_hour > 12:
        sec_part_day.append(i)
    elif cur_hour == 12:
        """неизвестно вклбчиельно 1 минута или нет, ставим включительно"""
        if cur_min >= 1:
            sec_part_day.append(i)
        else:
            fir_part_day.append(i)
    else:
        fir_part_day.append(i)

"""выводим данные"""
print(f'{len(fir_part_day)} станций остановилось с период с 00.00 до 12.00.')
print(f'{len(sec_part_day)} станций остановилось с период с 12.01 до 23.59.')
