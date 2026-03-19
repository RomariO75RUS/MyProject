print("Привет, давай знакомиться")
print("-"*30)

name = input("Как тебя зовут?")
age = input("Сколько тебе лет?")
city = input("Из какого ты города?")
color = input("Какой твой любимый цвет?")
height_cm = input("Какой у тебя рост в сантиметрах?")

print("-" *30)
print(f"очень приятно, {name}!")
print(f"Тебе {age} лет, и ты живешь в городе {city}.")
print("-" * 30)

age_numder = int(age)
height_m = float(height_cm) / 100
print(f"Через 5 лет тебе будет {age_numder + 5} лет/года.")
age_numder1 = age_numder - 10
if age_numder1 <= 0:
    print("10 лет назад ты еще не родился!")
else:
    print(f"10 лет назад тебе было {age_numder1} лет")


print("-" * 30)

if age_numder >= 18:
    print("Ты уже совершеннолетний")
else:
    years_left = 18 - age_numder
    print(f"Тебе еще {years_left} год(а) до совершенолетия.")

print(f"Твой любимый цвет {color}!")
print(f"Твой рост {height_m:2f} метра!")