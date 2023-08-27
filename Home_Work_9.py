# Напишите следующие функции:
# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.


import csv
from io import SEEK_CUR
import json
import opcode
import random


def one_deco(func: callable):
    number_generation()
    with open('file_for_QE.csv', 'r', newline='') as f_csv:
        a_b_c = f_csv.read().split('\n') 
    def wrapper():
        answer_list = []
        example = []
        count = 1
        for line in a_b_c[1:]:
            example = []
            if len(line) > 0:
                a, b, c = line.split(',')
                example.append(line)
                example.append(func(int(a), int(b), int(c)))
                answer_list.append(example)
        return answer_list
    return wrapper

def number_generation():
    count_str = random.randint(100,1001)
    csv_file = []
    for i in range(count_str):
        a = random.randint(0, 1000000)
        b = random.randint(0, 1000000)
        c = random.randint(0, 1000000)
        csv_str = [a, b, c]
        csv_file.append(csv_str)
    head_csv = ['a', 'b', 'c']
    with open('file_for_QE.csv', 'w') as f:
        csv.writer(f).writerow(head_csv)
        csv.writer(f).writerows(csv_file)

def two_deco(func: callable):
    def wrapper():
        file_json = {}
        end_fun = func()
        number = 2
        for line in end_fun:
            file_json.update({number: {}})
            for one in line:
                if len(one) > 2:
                    one_1 = one.replace('\r', '')
                    a, b, c = one_1.split(',')
                    file_json[number].update({'a': a})
                    file_json[number].update({'b': b})
                    file_json[number].update({'c': c})
                elif len(one) == 2:
                    *_, q = one[0].split('=')
                    file_json[number].update({'x1': q})
                    *_, q = one[1].split('=')
                    file_json[number].update({'x2': q})
                else:
                    if '=' in one:
                        *_, q = one[1].split('=')
                        file_json[number].update({'x': q})
                    else:
                        file_json[number].update({'x': one})
            number += 1
        with open('answer.json', 'w', encoding='utf-8') as f:
            json.dump(file_json, f, indent=4, ensure_ascii=False)
        return None
    return wrapper


    


@two_deco
@one_deco
def quadratic_equation(a: int, b: int, c: int) -> list:
    answer = []
    des = ((b**2) - 4*a*c)
    if des < 0:
        answer.append('no equation roots')
        return answer
    elif des == 0:
        answer.append(f'x = {((-b + (des**0.5))/2*a)}')
        return answer
    else:
        answer.append(f'x1 = {((-b + (des**0.5))/(2*a))}')
        answer.append(f'x2 = {((-b - (des**0.5))/(2*a))}')
        return answer


quadratic_equation()

# number_generation()