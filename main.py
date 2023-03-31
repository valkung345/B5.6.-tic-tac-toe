def greetings():
    print('Игра в крестики нолики       ')
    print('Введите два числа через пробел')
    print('Первое число - номер строки     ')
    print('Второе - номер столбца    ')
    print('Первым ходит крестик, вторым - нолик    ')


field = [[" "] * 3 for i in range(3)]


def board():
    print()
    print(f'  0 1 2')
    for i in range(3):
        row_info = " ".join(field[i])
        print(f"{i} {row_info}")


def check_input():
    while True:
        coord = input('Ваш ход: ').split()
        if len(coord) != 2:
            print('Введите два числа ')
            continue

        x, y = coord
        if not (x.isdigit()) or not (y.isdigit()):
            print('Введите два числа ')
            continue

        x, y = int(x), int(y)
        if x < 0 or x > 2 or 0 > y or y > 2:
            print('Числа не могут быть меньше 0 и больше 2 ')
            continue

        if field[x][y] != ' ':
            print('Клетка уже занята ')
            continue

        return x, y


def check_win():
    win_coord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                 ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                 ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for coord in win_coord:
        x_or_y = []
        for c in coord:
            x_or_y.append(field[c[0]][c[1]])
        if x_or_y == ["X", "X", "X"]:
            board()
            print("Победа за крестиком")
            return True
        if x_or_y == ["O", "O", "O"]:
            board()
            print("Победа за ноликом")
            return True
    return False


greetings()
count = 0
while True:
    count += 1
    board()
    if count % 2 == 1:
        print('Ход крестика')
    else:
        print('Ход нолика')

    x, y = check_input()
    if count % 2 == 1:
        field[x][y] = 'X'
    else:
        field[x][y] = 'O'

    if check_win():
        break
    if count == 9:
        print('Ничья')
        break
