num = 7

while True:
    p_number = int(input('Угадайте цифру(0-9): '))
    if p_number == num:
        print("Поздравляю! Вы угадали")
        break
    else:
        print("попробуйте снова")
