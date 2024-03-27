import csv


with open('new_time.csv', encoding='utf8') as f:
    """открываем и записываем файл"""
    reader = list(csv.reader(f, delimiter=','))[1:]


"""данные которые вводит пользователь"""
data = input()
while data != 'none':
    """ищем за o(n) и выводим"""
    for i in reader:
        if i[2] == data:
            print(f'В каюте {i[2]} восстановлено время (время остановки: {i[-2]}).')
            print(f'Актуальное время: {i[-1]}')
            break
    else:
        print('В этой каюте все хорошо')
    """обновляем данные из консоли"""
    data = input()
