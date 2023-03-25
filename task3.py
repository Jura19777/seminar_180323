"""
3. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""

def func(firstname, lastname, yearofbirth, city, email, telefon):
    print(f"{firstname} {lastname} {yearofbirth} года рождения, проживает в городе {city}, email: {email}, телефон: {telefon}")

func(firstname = "Иван", lastname = "Иванов", yearofbirth = 1846, city = "Москва", email = "jackie@gmail.com", telefon = "+7-100-532-14-56")