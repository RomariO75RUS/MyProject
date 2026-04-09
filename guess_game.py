import random
import sys
wins = 0
losses = 0
      
#Создание уровней
while True:

    print("Добро подаловать в игру Угадай число")
    print("=" *50)
    print('ВЫБЕРИТЕ СЛОЖНОСТЬ:')
    print('--Легкий(числа от 1 до 50, 15 попыток)')
    print('--Средний(числа от 1 до 100, 10 попыток)')
    print('--Сложный(числа от 1 до 200, 7 попыток)')
    print('--Нажми "0" для выхода из игры')

    complexity = input('Твой ввыбор(от 1 до 3): ')

    if complexity == '0':
        print(f"🏆 Игра завершена! Ты выиграл {wins} раз(а)!")
        sys.exit()  # ← немедленно закрывает программу

    if complexity == '1':
        max_number = 50
        max_attempts = 15
        level_name = 'Легкий'
    elif complexity == '2':
        max_number = 100
        max_attempts = 10
        level_name = 'Средний'
    elif complexity == '3':
        max_number = 200
        max_attempts = 7
        level_name = 'Сложный'
    else:
        print('Не верный выбор, играем на среднем!')
        max_number = 100
        max_attempts = 10
        level_name = 'Средний'
        
        

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
            
            break
    else:
        losses += 1
        print(f"Ты проиграл. Загадочное число было {secret_number}.")

    print("=" *50)
    print("Спасибо за игру!")


    again = input("Хочешь сыграть еще? ")
    if again != "да":
        print (f"Поздравляю! Ты выиграл {wins} раз! И проиграл {losses} раз!")
        sys.exit()
        