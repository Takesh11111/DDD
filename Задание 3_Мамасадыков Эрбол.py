import random

secret = 67
attempts = 7

while attempts > 0:
    guess = int(input("Введите число: "))

    if guess < secret:
        print("Загаданное число больше")
    elif guess > secret:
        print("Загаданное число меньше")
    else:
        print("Вы победили!")
        break

    attempts -= 1
    print("Осталось попыток:", attempts)

if attempts == 0:
    print("Вы проиграли.")
    print("Загаданное число:", secret)