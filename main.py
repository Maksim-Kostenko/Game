import random

class Person:
    __next_id = 1

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance.id = cls.__next_id
        cls.__next_id += 1
        return instance

    def __init__(self):
        self.__name = None

    @property
    def username(self):
        return self.__name

    @username.setter
    def username(self, value):
        if not value:
            raise ValueError('Имя не может быть пустым!')
        self.__name = value

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


def choose_first_player(pla):
    print('Выбирите игрока, кто будет делать первый ход:'
          '1-Выбрать игрока, который будет делать первый ход случайным образом.')

    selected_option = int(input())

    if selected_option == 1:
        result_option = random.choice([player_1.username, player_2.username])
        print(f'{result_option} делает первый ход')


register_players()

