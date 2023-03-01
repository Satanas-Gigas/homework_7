from pprint import pprint
import operator

#Задача №1

with open('recipes.txt', 'r', encoding='utf-8') as text:
    cook_book = {}
    while True:
        key = text.readline().strip()
        if not key:
            break
        cook_book[key] = []
        ingredient_count = int(text.readline().strip())
        for line in range(ingredient_count):
            ingredient = text.readline().split('|')
            cook_book[key] += [{'ingredient_name': ingredient[0].strip(), 'quantity': ingredient[1].strip(),\
                               'measure': ingredient[2].strip()}]
        text.readline()

pprint (cook_book, sort_dicts=False)
print()

#Задача №2

def get_shop_list_by_dishes(dishes, person_count):

    order = {}

    for dish in dishes:
        if dish not in cook_book.keys():
            return (f'В нашем ресторане блюдо {dish} не готовят')
        else:
            for ingredient in cook_book[dish]:
                order[ingredient['ingredient_name']] = {'measure': ingredient['measure'], 'quantity': 0}
                order[ingredient['ingredient_name']]['quantity'] += int(ingredient['quantity']) * person_count
    return order

order_dishes = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
pprint (order_dishes, sort_dicts=False)
print()


#Задача №3

file_list = {}
with open('1.txt', encoding='utf-8') as file1:
    file_one = len(file1.readlines())

file_list[file1.name] = file_one

with open('2.txt', encoding='utf-8') as file2:
    file_two = len(file2.readlines())

file_list[file2.name] = file_two

with open('3.txt', encoding='utf-8') as file3:
    file_three = len(file3.readlines())

file_list[file3.name] = file_three
tuples_sorted_file = sorted(file_list.items(), key=operator.itemgetter(1))
list_sorted_file = {k: v for k,v in tuples_sorted_file}
result = 'homework.txt'

for key, value in list_sorted_file.items():
    with open(f'{key}', encoding='utf-8') as file:
        read_file = file.read()
        with open(result, 'a') as file:
            file.write(f'{key}\n')
            file.write(f'{value}\n')
            file.write(f'{read_file}\n')
