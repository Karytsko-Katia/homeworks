weight = int(input("Введите свой вес, кг: "))
hight = int(input("Введите свой рост, см: "))
BMI = weight/(hight/100)**2
print(f"Ваш индекс массы тела: {BMI}")
step = "="
a = int(BMI - 10) * step
b = int(50 - BMI) * step
scale = ["10", a, "|", b, "50"]
print(''.join(scale))