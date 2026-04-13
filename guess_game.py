import random
import sys
wins = 0
losses = 0
highscores = [] # Таблица рекордов
print("Добро пожаловать в игру Угадай число")      
#Функция Таблицы рекордов
def show_records():
    if highscores:
        print(f'\n Таблица рекордов (лучшие результаты):')
        for i, (attempts, level) in enumerate(highscores):
            print(f'   {i+1}. {attempts} попыток ({level})')    
    else:
        print('\n Пока нет рекордов. Стань первым! \n')
        print ('=' * 40)

# Меню выбора сложности Функция
def show_menu():
    print("=" *50)
    print('ВЫБЕРИТЕ СЛОЖНОСТЬ:')
    print('--Легкий(числа от 1 до 50, 15 попыток(нажми 1))')
    print('--Средний(числа от 1 до 100, 10 попыток(нажми 2))')
    print('--Сложный(числа от 1 до 200, 7 попыток(нажми 3))')
    print('=' * 40)
    print('--Нажми "0" для выхода из игры')
    print('--Посмотреть таблицу рекордов(нажми 4)')
    print('=' * 50)
    complexity = input('Твой выбор(от 1 до 3): ')
    if complexity == '0':
        print(f"🏆 Игра завершена! Ты выиграл {wins} раз(а)!")
        sys.exit()  # ← немедленно закрывает программу

    if complexity == '1':
        return 50, 15, 'Легкий'
    elif complexity == '2':
        return 100, 10, 'Средний'
    elif complexity == '3':
        return 200, 7, 'Сложный'
    elif complexity == '4':
        show_records()
        return None, None, None
    else:
        print('Не верный выбор, играем на среднем!')
        return 100, 10, 'Средний'
    
#Создание уровней
while True:
    max_number, max_attempts, level_name = show_menu()
    if max_number is None:
        continue
    #Запуск игры
    secret_number = random.randint(1, max_number)
    attempts = 0
    print(f'Ты выбрал уровень : {level_name}')
    print(f"Я загадал число от 1 до {max_number}. У тебя {max_attempts} попыток!")
    print("=" * 50)

    while attempts < max_attempts:
        guess = input("Твое предположение: ")
        print('-' * 50)

        if not guess.isdigit():
            print("Это не число! Попробуй еще раз!")
            continue

        guess = int(guess)
        attempts += 1

        if guess < 1 or guess > max_number:
            print(f"Число должно быть от 1 до {max_number}!")
            print('-' * 50)
        elif guess < secret_number:
            if abs(guess - secret_number) < 5:
                print(f'Горячо! Разница всего {abs(guess-secret_number)}')
            print(f"Загаданное число больше. Попыток осталось: {max_attempts - attempts}")
            print('-' * 50)
        elif guess > secret_number:
            if abs(guess - secret_number) < 5:
                print(f"Горячо! Разница всего {abs(guess - secret_number)}")
            print(f"Загаданное число меньше. Осталось попыток: {max_attempts - attempts}")
            print('-' * 50)
        else:
            print(f"Поздравляю ты угадал число {secret_number} за {attempts} попыток!")
            wins += 1
            highscores.append((attempts, level_name))
            
            highscores.sort()
            if len(highscores) > 5:
                highscores.pop()
            
            break
    else:
        losses += 1
        print(f"Ты проиграл. Загадочное число было {secret_number}.")

    print("=" *50)
    #print("Спасибо за игру!")


    again = input("Хочешь сыграть еще? ")
    if again != "да":
        # Показать текущие рекорды
        show_records()
        print (f"Поздравляю! Ты выиграл {wins} раз! И проиграл {losses} раз!")
        sys.exit()
        