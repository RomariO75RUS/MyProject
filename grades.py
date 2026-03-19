print("Школьный помощник по оценкам")
print("-" * 40)

name = input("Как тебя зовут? ")
points = input("Сколько баллов в тесте ты набрал (от 0 до 100)? ")
subject = input("Какой предмет ты сдавал? ")

print("-" * 40)

points = int(points)

if points >= 101:
    grade = "ошибка"
    comment = "Баллов не может быть больше 100, ты лжец!"
elif points >= 90:
    grade = 5
    comment = "Отличный результат, продолжай в том же духе!"
elif points >= 80:
    grade = 4
    comment = "Тоже хорошая оценка, тебе не хватило совсем чуть-чуть!"
elif points >= 60:
    grade = 3
    comment = "Не самый плохой вариант, но ты должен стараться!"
elif points >= 30:
    grade = 2
    comment = "Очень плохо, месяц без КОМПЬЮТЕРА!!!!!"
else:
    grade = "ошибка"
    comment = "Напиши баллы корректно!"



print(f"{name}, твой результат:")
print(f"Твой балл: {points}!")
print(f"Твоя оценка: {grade}!")
print(f"Комментарий: {comment}")
print(f"По предмету {subject} ты получил(а) {grade}!")

print("-" * 40)

if points == 100:
    print("Лучший в мире за работой! ПЕРФЕКТО!!! ТЫ ГЕНИЙ!!!")
elif points == 0:
    print("Я ожидал от тебя достойного результата, ты наказан!")

