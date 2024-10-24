import random

list = [1, 2, 3, 4, 5, 6]
user_num = int(input('Введите число: '))
guessed_num = None

while guessed_num != user_num:
    guessed_num = random.choice(list)
    if guessed_num == user_num:
        print("Я угадал число, и это число " + str(user_num))
    else:
        print(f"Я не угадал, выбрал {guessed_num}, попробую ещё раз...")
