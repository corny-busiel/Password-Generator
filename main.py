import hashlib
import getpass
import random
import string

# Функцыя для ўводу дадзеных ад карыстальніка
def input_user():
    user_site = input("Увядзіце веб-сайт: ")  # Уваходныя даныя: веб-сайт
    user_name = input("Увядзіце імя карыстальніка: ")  # Уваходныя даныя: імя карыстальніка
    user_password = getpass.getpass("Увядзіце пароль: ")  # Уваходныя даныя: пароль
    user_rounds = int(input("Увядзіце колькасць раундоў: "))  # Уваходныя даныя: колькасць раундаў
    user_len_password = int(input("Увядзіце даўжыню пароля: "))  # Уваходныя даныя: даўжыня пароля
    return {
        "site": user_site,
        "name": user_name,
        "password": user_password,
        "rounds": user_rounds,
        "len_password": user_len_password
    }

# Функцыя для генерацыі хэша пароля
def password_generation_hash(user_data):
    user_pass_generator = hashlib.sha256(user_data["password"].encode("utf-8")).hexdigest()  # Генеруем хэш пароля
    for _ in range(user_data["rounds"]):
        user_pass_generator = hashlib.sha512(user_pass_generator.encode("utf-8")).hexdigest()  # Прымяняем алгарытм некалькіх раундаў
    return user_pass_generator

# Функцыя для генерацыі канчатковага пароля
def password_finaly_generation(user_pass_generator):
    random.seed(42)  # Ініцыялізуем генератар выпадковых лікаў з пастаянным семенем
    symbols = string.punctuation  # Знакі пунктуацыі для стварэння пароля
    range_symbols = random.randint(0, len(symbols) - 1)  # Выбіраем случайную колькасць знакаў пунктуацыі
    user_pass_generator = list(user_pass_generator)  # Ператвараем хэш у спіс знакаў
    for i in range(range_symbols):
        user_pass_generator.insert(range_symbols, symbols[i])  # Уставляем случайныя знакі пунктуацыі ў хэш
    for i in range(range_symbols):
        user_pass_generator[i] = user_pass_generator[i].upper()  # Змяняем вялікія літары
    password_finally = "".join(user_pass_generator)  # Склеіць знакі у канчатковы пароль
    return password_finally

# Галоўная функцыя
def main():
    user_data = input_user()  # Увод дадзеных ад карыстальніка
    password_finaly = password_generation_hash(user_data)  # Генерацыя хэша пароля
    print(f"Выход: {password_finaly_generation(password_finaly[:user_data['len_password']])}")  # Вывад канчатковага пароля
    
if __name__ == "__main__":
    main()
