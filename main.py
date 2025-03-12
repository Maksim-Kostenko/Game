# from random import randint
# import time
#
# def game():
#
#     name_first_player = input('Введите имя первого игрока: ')
#     name_second_player = input('Введите имя второго игрока: ')
#
#     #Добавить проверку имен, что бы они были разные
#
#     print("Выберите способ определение того, кто начнет игру первым: ")
#     print("1- Я сделаю ход первым;"
#           "2- Соперник сделает ход первым;"
#           "3- Выбрать рандомно.")
#     decision_first_player = f'{name_first_player} выберите вариант от 1 до 3: '
#     decision_second_player = f'{name_second_player} выберите вариант от 1 до 3: '
#
#     first_move_player = None
#     winner_game = None
#
#     if (decision_first_player == 1 and decision_second_player == 2) or (decision_first_player == 2 and decision_second_player == 1):
#         if decision_first_player == 1:
#             print(f'{name_first_player} делает первый ход.')
#             first_move_player = 1
#         else:
#             print(f'{name_second_player} делает первый ход.')
#             first_move_player = 2
#     else:
#         print(f'Выбор игрока произойдет рандомно...'
#               f'Происходит выбор подождите 2 секунды...')
#         randint_first_player, randint_second_player = randint(1, 100), randint(1, 100)
#         time.sleep(2)
#         if randint_first_player < randint_second_player:
#             first_move_player = 2
#             print(f'{name_second_player} делает первый ход.')
#         else:
#             first_move_player = 1
#             print(f'{name_first_player} делает первый ход.')
#
#         game_map = [['-','-','-'], ['-','-','-'], ['-','-','-']]
#         for string in game_map:
#             for s in string:
#                 print(s)
#
#
# game()
