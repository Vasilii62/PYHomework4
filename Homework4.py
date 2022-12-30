# Задача 1: Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# Вариант 1

# def calc_pi(eps=1.0e-5):
#     s=0
#     d=1
#     sgn=1
#     while True:
#         a=4/d
#         s=s+sgn*a
#         if a<eps:
#             return s
#         sgn=-sgn
#         d=d+2
 
# print(round(calc_pi(), 3))

# Вариант 2

# import math

# print(round(math.pi, 3))

# Вариант 3

# from math import factorial
# from decimal import *
# def chudnovsky(n):
#     pi = Decimal(0)
#     k = 0
#     while k < n:
#         pi += (Decimal(-1)**k) * (Decimal(factorial(6 * k)) / ((factorial(k)**3) * (factorial(3*k))) * (13591409 + 545140134 * k) / (640320**(3 * k)))
#         k += 1
#     pi = pi * Decimal(10005).sqrt() / 4270934400
#     pi = pi**(-1)
#     return pi

# N = 10
# getcontext().prec = N
# val = chudnovsky(N / 14)
# print(round(val, 3))


# Задача 2: Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

# Вариант 1

# num = int(input('Enter a number: '))
# i = 2
# my_list = []
# x = num
# while i <= num:
#     if num % i == 0:
#         my_list.append(i)
#         num //= i
#         i = 2
#     else:
#         i += 1

# print(f'Prime factors of the number {x}: {my_list}')

# Вариант 2

# def prime_check(x):
#     k = 0
#     for i in range(2, int(x**0.5)+1):
#             if (x % i == 0):
#                 k = k+1
#     if k == 0:
#         return True
#     else:
#         return False

# def main():
#     N = 824

#     print(f"Prime factors of the number {N}:")
#     for i in range(2, N+1):
#         if N % i == 0:
#             if prime_check(i):
#                 print(i, end=' ')

# if __name__ == "__main__":
#     main()

# Задача 3: Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

# Вариант 1

# my_list = list(map(int, input('Enter numbers with a space: ').split()))
# print(f'Source list: {my_list}')
# new_list =[]
# [new_list.append(i) for i in my_list if i not in new_list]
# print(f'List of non-repeating elements: {new_list}')

# Вариант 2

# my_list = list(map(int, input('Enter numbers with a space: ').split()))
# new_list = list(set(my_list))
# print(new_list)

# Задача 4: Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# *Пример:* 

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0 

# import random


# def write_file(exp):
#     with open('file2.txt', 'w') as data:
#         data.write(exp)


# def rnd():
#     return random.randint(0, 101)


# def create_pol(k):
#     lst = [rnd() for i in range(k+1)]
#     return lst


# def create_str(sp):
#     my_list = sp[::-1]
#     wr = ''
#     if len(my_list) < 1:
#         wr = 'x = 0'
#     else:
#         for i in range(len(my_list)):
#             if i != len(my_list) - 1 and my_list[i] != 0 and i != len(my_list) - 2:
#                 wr += f'{my_list[i]}x^{len(my_list)-i-1}'
#                 if my_list[i+1] != 0:
#                     wr += ' + '
#             elif i == len(my_list) - 2 and my_list[i] != 0:
#                 wr += f'{my_list[i]}x'
#                 if my_list[i+1] != 0:
#                     wr += ' + '
#             elif i == len(my_list) - 1 and my_list[i] != 0:
#                 wr += f'{my_list[i]} = 0'
#             elif i == len(my_list) - 1 and my_list[i] == 0:
#                 wr += ' = 0'
#     return wr


# k = int(input("Введите натуральную степень k = "))
# koef = create_pol(k)
# write_file(create_str(koef))
# print(koef)
# print(create_str(koef))

# Задача 5: Даны два файла, в каждом из которых находится запись
# многочлена. Задача - сформировать файл, содержащий сумму многочленов.

import random

def write_file(name, st):
    with open(name, 'w') as data:
        data.write(st)

def rnd():
    return random.randint(0, 101)

def create_mn(k):
    my_list = [rnd() for i in range(k+1)]
    return my_list

def create_str(sp):
    my_list = sp[::-1]
    wr = ''
    if len(my_list) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(my_list)):
            if i != len(my_list) - 1 and my_list[i] != 0 and i != len(my_list) - 2:
                wr += f'{my_list[i]}x^{len(my_list)-i-1}'
                if my_list[i+1] != 0 or my_list[i+2] != 0:
                    wr += ' + '
                elif i == len(my_list) - 2 and my_list[i + 2] != 0:
                    wr += f'{my_list[i]}x'
                    if my_list[i+1] != 0 or my_list[i+2] != 0:
                        wr += ' + '
                elif i == len(my_list) - 1 and my_list[i] != 0:
                    wr += f'{my_list[i]} = 0'
                elif i == len(my_list) - 1 and my_list[i] == 0:
                    wr += ' = 0 '
    return wr

def sq_mn(k):
    if 'x^' in k:
        i = k.find('^')
        num = int(k[i+1:])
    elif ('x' in k) and ('^' not in k):
        num = 1
    else:
        num = - 1
    return num

def k_mn(k):
    if 'x' in k:
        i = k.find('x')
        num = int(k[:i])
    return num

def calc_mn(st):
    st = st[0].replace(' ', '').split('=')
    st = st[0].split('+')
    my_list = []
    l = len(st)
    k = 0
    if sq_mn(st[-1]) == -1:
        my_list.append(st[-1])
        l -= 1
        k = 1
    i = 1
    ii = l-1
    while ii >= 0:
        if sq_mn(st[ii]) != -1 and sq_mn(st[ii]) == i:
            my_list.append(k_mn(st[ii]))
            ii -= 1
            i += 1
        else:
            my_list.append(0)
            i += 1
    return my_list

k1 = int(input('Enter the natural degree for the first file k: '))
k2 = int(input('Enter the natural degree for the second file k: '))
koef1 = create_mn(k1)
koef2 = create_mn(k2)
write_file('file4_1.txt', create_str(koef1))
write_file('file4_2.txt', create_str(koef2))

with open('file4_1.txt', 'r') as data:
    st1 = data.readlines()
with open('file4_2.txt', 'r') as data:
    st2 = data.readlines() 
print(f'First polynomial: {st1}')
print(f'Second polynomial: {st2}')
my_list1 = calc_mn(st1)   
my_list2 = calc_mn(st2)
ll = len(my_list1)
if len(my_list1) > len(my_list2):
    ll = len(my_list2)
new_list =[my_list1[i] + my_list2[i] for i in range(ll)]
if len(my_list1) > len(my_list2):
    mm = len(my_list1)
    for i in range(ll, mm):
        new_list.append(my_list1[i])
else:
    mm = len(my_list2)
    for i in range(ll, mm):
        new_list.append(my_list2[i])
write_file('file4_res.txt', create_str(new_list))
with open('file4_res.txt', 'r') as data:
    st3 = data.readlines()
    print(f'Sum of polynomials: {st3}')

