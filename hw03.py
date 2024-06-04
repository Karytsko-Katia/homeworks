import os
import random
print("Привет! Это игра 'Кто хочет стать миллионером!'Хочешь поучавствовать?")
entrance = input("Если готов - жми 'y'! Не готов - жми 'n'!")
if entrance == "y":
    print("Погнали!")
else:
    print("Приходи когда будешь смел!")
input('Нажмите ENTER для продолжения!')
os.system('clear')
questions = {"Самая большая планета солнечной системы это?": ["Марс", "Юпитер", "Уран", "Плутон"], 
            "Как называется верхняя часть пирамиды?": ["Основание", "Вершина", "Грань", "Топчик"], 
            "Какое животное является символом США?": ["Лев", "Пингвин", "Орел", "Медведь"],
            "Какое из этих животных не является млекопитающим?": ["Кит", "Пингвин", "Дельфин", "Летучая мышь"],
            "Какая страна известна как родина Олимпийских игр?": ["Армения", "Греция", "Египет", "Италия"],
            "Как называется прибор для измерения температуры?": ["Термометр", "Барометр", "Гигрометр", "Спидометр"],
            "У какого морского животного 8 щупалец?": ["Осьминог", "Аквалангист", "Кальмар", "Каракатица"],
            "Какое из этих животных не умеет прыгать?": ["Лошадь", "Кенгуру", "Жаба", "Слон"],
            "Какое из этих животных не живет в Африке?": ["Жираф", "Тигр", "Лев", "Зебра"]}
corr_answers = {"Самая большая планета солнечной системы это?": "Юпитер", 
                "Как называется верхняя часть пирамиды?": "Вершина", 
                "Какое животное является символом США?": "Орел",
                "Какое из этих животных не является млекопитающим?": "Пингвин",
                "Какая страна известна как родина Олимпийских игр?": "Греция",
                "Как называется прибор для измерения температуры?": "Термометр",
                "У какого морского животного 8 щупалец?": "Осьминог",
                "Какое из этих животных не умеет прыгать?": "Слон",
                "Какое из этих животных не живет в Африке?": "Тигр"}
hints = ["ЗД", "50/50", "ПЗ"]
money = 0
s = 0
while s <= len(questions)-1:
    print(list(questions.keys())[s])
    answers = questions[(list(questions.keys())[s])]
    random.shuffle(answers)
    for i, a in enumerate(answers):
        print(f'{i + 1}: {a}')
    print('Если хотите использовать посказку - жмите 5!')
    answer = int(input("Введите номер ответа? "))
    if answers[answer - 1] == corr_answers[(list(corr_answers.keys())[s])]:
        print("И это правильный ответ!")
        money += 1000000 // len(questions)
        print(f'Ваш выйгрыш - {money} !')
        input('Нажмите ENTER для продолжения!')
        os.system('clear')
        s += 1
    else:
        print('Это не правильный ответ! Игра окончена!')
        print(f'Ваш выйгрыш - {money} !')
        break
print("YOU ARE WINNER!" )