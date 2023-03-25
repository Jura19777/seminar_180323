"""
1. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""

month_list = [['Зима', 12, 1, 2], ['Весна', 3, 4, 5], ['Лето', 6, 7, 8], ['Осень', 9, 10, 11]]

month_num = int(input('Введите порядковый номер месяца в году (1..12): '))
if month_num in range(1, 13):
    for i, el in enumerate(month_list):
        if month_num in el[1:4]:
            print(f'Результат через список: Введенный номер месяца относится к сезону {el[0]}')
            break
else:
    print('Введен некорректный номер месяца!')

month_dict = {'Зима': [12, 1, 2], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}

if month_num in range(1, 13):
    for i, el in month_dict.items():
        if month_num in el[:]:
            print(f'Результат через словарь: Введенный номер месяца относится к сезону {i}')
            break
else:
    print('Введен некорректный номер месяца!')