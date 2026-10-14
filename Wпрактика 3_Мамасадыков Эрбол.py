#задание 1


#flags = {
#    'ru': {'red blue', 'white'},
#    'kg': {'red yellow', 'red'},
#    'ua': {'red blue', 'red', 'blue'},
#    'uk': {'yellow', 'blue'},
#   'kz': {'blue yellow', 'blue'},
#   'nz': {'white', 'red', 'blue'},
#   'jp': {'white', 'red'},
#   'pk': {'green', 'white',}
#

#while True:
#    print("\nВведите цвета флага.")
#    print("Если хотите выйти напишите: выход")
#    color1 = input("Напишите первый цвет: ").lower()

#    if color1 == 'выход':
#        print("Процесс завершена.")
#        break

#    color2 = input("Напишите второй цвет: ").lower()

#    result = []

#    for domain, colors in flags.items():
#        all_colors = ' '.join(colors)

#        if color1 in all_colors and color2 in all_colors:
#            result.append(domain)

#    if result:
#        print("Флаг с такими цветами:", result)
#    else:
#        print("Подходящих флагов не найдено.")


#задание 2


#data_tuple = ('h', 6.13, 'C', ['e', 'T'], True, 'k', 'e', '3', 'e', 1, ('g', 'x'), False)

#letters = []
#numbers = []
#flags = []


#def process_item(item):
#    if isinstance(item, (list, tuple)):
#        for x in item:
#            process_item(x)

#    elif isinstance(item, bool):
#        flags.append(item)

#   elif isinstance(item, (int, float)):
#        numbers.append(item)

#    elif isinstance(item, str):
#        if item.isdigit():
#            numbers.append(int(item))
#        else:
#            letters.append(item)


#for item in data_tuple:
#    process_item(item)


#if 6.13 in numbers:
#    numbers.remove(6.13)


#index_3 = numbers.index(3)
#index_1 = numbers.index(1)

#middle = max(index_3, index_1)
#numbers.insert(middle, 2)


#numbers.sort(reverse=True)


#letters = letters[::-1]


#letters = [x.swapcase() for x in letters]


#letters.extend(flags)


#result = list("Cheetah")

#result.extend(flags)


#print("letters:", letters)
#print("numbers:", numbers)
#print("result:", result)














