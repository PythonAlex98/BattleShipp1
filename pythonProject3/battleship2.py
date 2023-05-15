from random import randint

# Размер поля
SIZE = 6

# Количество кораблей
SHIP_COUNT = 3

# Отображение поля
HIDDEN = '-'
SHIP = 'O'
MISS = '.'
HIT = 'X'

# Инициализация поля
player_field = [[HIDDEN for j in range(SIZE)] for i in range(SIZE)]
bot_field = [[HIDDEN for j in range(SIZE)] for i in range(SIZE)]

# Размещение кораблей на поле
def place_ships(field):
    ships = 0
    while ships < SHIP_COUNT:
        x = randint(0, SIZE-1)
        y = randint(0, SIZE-1)
        if field[x][y] != SHIP:
            field[x][y] = SHIP
            ships += 1

# Отображение поля
def print_field(field):
    print(" ", end="")
    for i in range(SIZE):
        print(i, end="")
    print()
    for i in range(SIZE):
        print(i, end="")
        for j in range(SIZE):
            print(field[i][j], end="")
        print()

# Проверка координат выстрела
def check_shot(x, y, field):
    if x < 0 or x >= SIZE or y < 0 or y >= SIZE:
        return False
    if field[x][y] == SHIP:
        field[x][y] = HIT
        return True
    elif field[x][y] == HIDDEN:
        field[x][y] = MISS
        return True
    else:
        return False

# Ход игрока
def player_turn():
    while True:
        print("Your turn:")
        x = int(input("Enter X coordinate: "))
        y = int(input("Enter Y coordinate: "))
        if check_shot(x, y, bot_field):
            print("Hit!")
            print_field(bot_field)
            if check_win(bot_field):
                print("You won!")
                exit()
            else:
                break
        else:
            print("Invalid input or already shot there. Try again.")

# Ход бота
def bot_turn():
    while True:
        print("Bot's turn:")
        x = randint(0, SIZE-1)
        y = randint(0, SIZE-1)
        if check_shot(x, y, player_field):
            print("Hit!")
            print_field(player_field)
            if check_win(player_field):
                print("Bot won!")
                exit()
            else:
                break

# Проверка на победу
def check_win(field):
    for i in range(SIZE):
        for j in range(SIZE):
            if field[i][j] == SHIP:
                return False
    return True

# Игровой процесс
def game():
    place_ships(player_field)
    place_ships(bot_field)
    while True:
        player_turn()
        bot_turn()

# Запуск игры
game()
