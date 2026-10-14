num_1 = float(input('Введите температуру Чуйской области'))
num_2 = float(input('Введите температуру Иссык-кульской области'))
num_3 = float(input('Таласской области'))
num_4 = float(input('Нарынской области'))
num_5 = float(input('Джалала-абадской области'))
num_6 = float(input('Ошской области'))
num_7 = float(input('Бактенской области'))

res = (num_1+num_2+num_3+num_4+num_5+num_6+num_7)/7

res_float = round(res, 2) 
print(f' "Средняя погода в КР" {num_1}+{num_2}+{num_3}+{num_4}+{num_5}+{num_6}+{num_7}={res_float}')