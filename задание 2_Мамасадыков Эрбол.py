LOGIN = "admin"
PASSWORD = "12345"

attempts = 3

while attempts > 0:
    user_login = input("Введите логин: ")
    user_password = input("Введите пароль: ")

    # Проверка введенных данных
    if user_login == LOGIN and user_password == PASSWORD:
        print("Добро пожаловать!")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print("Неверный логин или пароль")
            print(f"Осталось попыток: {attempts}")
        else:
            print("Аккаунт заблокирован")