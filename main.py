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
        elif not value.isalpha():
            raise ValueError('Имя может содержать только буквы!')
        elif len(value) > 11:
            raise ValueError('Слишком длинное имя, максимальнав длина имени 10 букв!')
        self.__name = value.title()


player_1 = Person()
player_2 = Person()




def register_players():
    """Функция для регистрации игроков."""

    def get_player_name(player_id):
        """Запрашивает имя игрока."""
        return input(f'Введите имя игрока {player_id}: ')

    def set_player_username(player):
        """
        Функция реализует присваивание имени игрока к экземпляру класса переданного в качестве аргумента
        :param player: экземпляр класса Person
        :return: функция ничего не возвращает (None)
        """
        while not player.username:
            try:
                player.username = get_player_name(player.id)
            except ValueError as e:
                print(e)

    set_player_username(player_1)
    set_player_username(player_2)

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
    """ Функция выбора первого игрока(хотел реализовать выбор первого игрока по голосованию, но не хватило времени на это,
    оставил это на потом, при этом задание этого не требует)"""
    option = 'Выбирите способ определения игрока, который будет делать первый ход:\n1-Выбрать игрока случайным образом.'
    while True:
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
    """ Выводит изображения игрового поля в терминал"""
    print("-" * 13)
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-" * 13)

def reset_board(board):
    """Сбрасывает игровое поле для новой игры."""
    for i in range(9):
        board[i] = i + 1

def take_position(player_token, board, player):
    """Проверяет и устанаввливает Х или О на игровом поле"""
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
    """Проверяет наличие выйгрышных комбинаций на игровом поле"""
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def game(board, first_player, second_player):
    """Цикл реализующий процесс игры"""
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_position("X", board, first_player.username)
        else:
            take_position("O", board, second_player.username)
        counter += 1

        winner_token = check_win(board)
        if winner_token:
            if winner_token == "X":
                print(first_player.username, "выиграл!")
            else:
                print(second_player.username, "выиграл!")
            win = True
            break

        if counter == 9:
            print("Ничья!.")
            break
    draw_board(board)



def main():
    try:
        """Основная функция"""
        print('Добро пожаловать в игру "Крестики-нолики!"\nДавайте познакомимся!')
        register_players()
        print('Приступим к выбору игрока, который будет делать первый ход!')
        first_player, second_player = selection_first_player()
        print('Приступим к игре!')
        board = list(range(1, 10))
        game(board, first_player, second_player)

        while True:
            play_again = input("Хотите сыграть еще раз? (да/нет): ").lower()
            if play_again == "да":
                reset_board(board)
                first_player, second_player = selection_first_player()
                game(board, first_player, second_player)
            else:
                print("Спасибо за игру! До свидания!")
                break
    except KeyboardInterrupt:
        print('Игра завершена принудительно!')

if __name__ == '__main__':
    main()
