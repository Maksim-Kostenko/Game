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


result_selection_first_player = None

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
    global result_selection_first_player
    option = 'Выбирите способ определения игрока, который будет делать первый ход:\n1-Выбрать игрока случайным образом.'
    print(option)
    try:
        selected_option = int(input('Введите номер способа: '))
        if selected_option == 1:
            result_selection_first_player = random.choice([player_1.username, player_2.username])
            print(f'{result_selection_first_player} ходит первым!')
        else:
            raise ValueError(f'Некорректный выбор!'
                             f'Введите число из представленных способов'
                             f'{option}')
    except ValueError as e:
        print(e)

board = list(range(1, 10))

def draw_board(board_1):
    print("-" * 13)
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-" * 13)

def take_position(selection, first_player):
    pass



def main(board_1):
    win = False

    print('Добро пожаловать в игру "Крестики-нолики!"\nДавайте познакомимся!')
    register_players()
    print('Приступим к выбору игрока, который будет делать первый ход!')
    selection_first_player()
    print('Приступим к игре!')
    draw_board(board_1)

    while not win:
        pass


if __name__ == '__main__':
    main(board)
