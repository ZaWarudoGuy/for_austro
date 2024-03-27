import csv

with open('astronaut_time.txt', encoding='utf8') as file, open('new_time.csv', 'w', encoding='utf8', newline='') as new_file:

    """открываем файлы для записи и чтения"""
    writer = csv.writer(new_file, delimiter=',')
    dump = file.readlines()[1:]
    upload_data = [['WatchNumber', 'numberStation', 'cabinNumber', 'timeStop', 'timeNow']]

    """цикл для счета времени"""
    for i in dump:
        current_data = i.strip().split('>')
        cur_hour, cur_min, cur_sec = current_data[-2].split(':')
        timeNow = ''

        if int(cur_hour) + int(current_data[-1]) >= 24:
            cur_hour = str((int(cur_hour) + int(current_data[-1])) % 24)
            if len(cur_hour) == 1:
                cur_hour = '0' + cur_hour
        else:
            cur_hour = str((int(cur_hour) + int(current_data[-1])))
            if len(cur_hour) == 1:
                cur_hour = '0' + cur_hour

        current_data[-1] = f'{cur_hour}:{cur_min}:{cur_sec}'
        upload_data.append(current_data)

    """записываем данные"""
    for upload in upload_data:
        writer.writerow(upload)

    """выводим данные о кабине"""
    for i in upload_data:
        if i[2] == '98-OYE':
            print(f'{i[-1]} действительное время для каюты: {i[2]}')
