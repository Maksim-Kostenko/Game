import random

class Person:
    __next_id = 1
    instances = list()

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance.id = cls.__next_id
        cls.__next_id += 1
        return instance

    def __init__(self):
        self.__name = None
        Person.instances.append(self)

    @property
    def username(self):
        return self.__name

    @username.setter
    def username(self, value):
        if not value:
            raise ValueError('Имя не может быть пустым!')
        elif not value.isalpha():
            raise ValueError('Имя может содержать только буквы!')
        self.__name = value.title()

    @classmethod
    def get_instances(cls):
        return cls.instances

player_1 = Person()
player_2 = Person()




def register_players():

    def get_player_name(player_id):
        return input(f'Введите имя игрока {player_id}: ')


    while not player_1.username:
        try:
            player_1.username = get_player_name(player_1.id)
        except ValueError as e:
            print(e)

    while not player_2.username:
        try:
            player_2.username = get_player_name(player_2.id)
        except ValueError as e:
            print(e)

    while player_1.username == player_2.username:
        print('Имена игроков не должны быть одинаковыми!')
        try:
            num_player = int(input('Введите номер игрока, чье имя хотите изменить (1 или 2): '))
            if num_player == 1:
                player_1.username = get_player_name(player_1.id)
            elif num_player == 2:
                player_2.username = get_player_name(player_2.id)
            else:
                print("Некорректный номер игрока. Пожалуйста, введите 1 или 2.")
        except ValueError:
            print("Ошибка: введите число (1 или 2).")

    print(f"Игрок 1: {player_1.username}")
    print(f"Игрок 2: {player_2.username}")


def selection_first_player():
    """ Доделать нормально, сделать цикл"""
    option = 'Выбирите способ определения игрока, который будет делать первый ход:\n1-Выбрать игрока случайным образом.'
    print(option)
    try:
        selected_option = int(input('Введите номер способа: '))
        if selected_option == 1:
            first_player = random.choice([player_1, player_2])
            second_player = player_2 if first_player == player_1 else player_1
            print(f'{first_player.username} ходит первым!')
            return first_player, second_player
        else:
            raise ValueError(f'Некорректный выбор!'
                             f'Введите число из представленных способов'
                             f'{option}')
    except ValueError as e:
        print(e)



def draw_board(board):
    print("-" * 13)
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-" * 13)

def take_position(player_token, board, player):
    valid = False
    while not valid:
        player_answer = input(player + ",куда поставим " + player_token + "? ")
        try:
            player_answer = int(player_answer)
        except ValueError:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if 1 <= player_answer <= 9:
            if str(board[player_answer - 1]) not in "XO":
                board[player_answer - 1] = player_token
                valid = True
            else:
                print("Эта клетка уже занята!")
        else:
            print("Некорректный ввод. Введите число от 1 до 9.")

def check_win(board):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def game(board, first_player, second_player):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_position("X", board, first_player.username)
        else:
            take_position("O", board, second_player.username)
        counter += 1

        tmp = check_win(board)
        if tmp:
            if tmp == "X":
                print(first_player.username, "выиграл!")
            else:
                print(second_player.username, "выиграл!")
            win = True
            break
        else:
            print(first_player.username, "выиграл!")

        if counter == 9:
            print("Ничья!.")
            break
    draw_board(board)



def main():
    print('Добро пожаловать в игру "Крестики-нолики!"\nДавайте познакомимся!')
    register_players()
    print('Приступим к выбору игрока, который будет делать первый ход!')
    first_player, second_player = selection_first_player()
    print('Приступим к игре!')
    board = list(range(1, 10))
    game(board, first_player, second_player)


if __name__ == '__main__':
    main()
