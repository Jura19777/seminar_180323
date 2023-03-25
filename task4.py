"""
4. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""
def my_func1(a, b ,c):
    s = [a, b, c]
    s.sort(reverse=True)
    return s[0] + s[1]

def my_func2(a, b ,c):
    s = [a, b, c]
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if (s[j] < s[i]):
                x = s[i]
                s[i] = s[j]
                s[j] = x
    return s[2] + s[1]

print(my_func1(3, 5, 1))
print(my_func2(3, 5, 1))