# Программа для работы со списком рекордов

# Пустой список для рекордов
highscores = []

while True:
    print("\n" + "=" * 40)
    print("ТАБЛИЦА РЕКОРДОВ")
    print("=" * 40)
    
    # Показываем текущие рекорды
    if len(highscores) == 0:
        print("Пока нет рекордов. Сыграй и добавь!")
    else:
        print("Топ рекордов (чем меньше попыток, тем лучше):")
        for i, score in enumerate(highscores):
            print(f"{i+1}. {score} попыток")
    
    print("\nЧто хочешь сделать?")
    print("1 - Добавить новый рекорд")
    print("2 - Удалить последний рекорд")
    print("3 - Очистить все рекорды")
    print("0 - Выйти")
    
    choice = input("Твой выбор: ")
    
    if choice == "1":
        new_score = input("Введите количество попыток: ")
        if new_score.isdigit():
            new_score = int(new_score)
            highscores.append(new_score)
            highscores.sort()  # сортируем по возрастанию (меньше = лучше)
            if len(highscores) > 5:
                highscores.pop()  # оставляем только топ-5
            print(f"Рекорд {new_score} добавлен!")
        else:
            print("Нужно ввести число!")
    
    elif choice == "2":
        if highscores:
            removed = highscores.pop()
            print(f"Удалён рекорд: {removed}")
        else:
            print("Нет рекордов для удаления!")
    
    elif choice == "3":
        highscores.clear()
        print("Все рекорды очищены!")
    
    elif choice == "0":
        print("До свидания!")
        break
    
    else:
        print("Неверный выбор!")