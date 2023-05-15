from datetime import datetime
import re

from colorama import init
from colorama import Fore, Back
init()

topic_history_global = []
topic_history_user = []
topics_dictionary = {'математика': ["Обчислення площі трикутника за допомогою векторного добутку;",
                                    "Обчислення площі прямокутника;",
                                    "Виведення н-того числа Фібоначчі;",
                                    "Виведення числа π."],
                     'фізика': ["Закон збереження енергії;",
                                "Виведення сталої Планка;",
                                "Виведення кулонівської сталої."],
                     'географія': ["Де знаходиться Сахара - найбільша пустеля в світі?",
                                   "Які дві держави мають найбільшу кількість кордонів з іншими державами?",
                                   "Знаходження відстань між двома точками А(x1, y1) та В(x2, y2);",
                                   "Знаходження азимуту від точки А(x1, y1) до точки В(x2, y2)."],
                     'філологія': ["Яка різниця між іменником та прикметником?",
                                   "Які відмінки є в українській мові?"],
                     'астрономія': ["Які типи зір відомі в астрономії?",
                                    "Які планети Сонячної системи мають найбільші та найменші орбіти?"],
                     'загальні запитання': ["Котра година?",
                                            "Який зараз місяць?",
                                            "Який зараз рік?",
                                            "Яка зараз пора року?",
                                            "Скільки днів до Нового Року?",
                                            "Пограти у камінь-ножиці-папір;",
                                            "Як тебе звати?",
                                            "Заспівати колядку;",
                                            "Сказати надихаючу цитату;",
                                            "Розповісти анекдот."],}

def mathem():
    subtopics = topics_dictionary['математика']

    output = ""
    for i in range(len(subtopics)):
        output += (str(i + 1) + ". " + subtopics[i] + "\n")

    print_response(f'Ви прицюєте в блоці: ' + Fore.BLUE + '"математика"' + Fore.RESET + '.\n' + Fore.RED +
f'!' + Fore.RESET + 'при необхідності, Ви можете скористатися функціями: "допомога", "назад" та "вихід"'+ Fore.RED +'!\n'
                   + Fore.BLUE +f'Список доступних підтем:\n'+ Fore.RESET +
                   f'{output}'
                   f'Введи номер однієї з підтем, допомога з якою тобі потрібна: ')
    while True:

        subtopic_number = get_user_input()
        topic_history_global.append(f"[User]: {subtopic_number}")

        if subtopic_number == 'допомога':
            print_help()
            break

        if subtopic_number == 'назад':
            print_greeting()
            break

        if subtopic_number == 'вихід':
            print_exit()

        if subtopic_number == '1':
            import numpy as np

            while True:
                try:
                    print_response("Для початку обчислення площі трикутника, \n" + Fore.BLUE +
f"""введіть координати точки A через пробіл: """ + Fore.RESET)
                    x1, y1 = map(float, get_user_input().split())

                    print_response(Fore.BLUE + "Введіть координати точки B через пробіл: " + Fore.RESET)
                    x2, y2 = map(float, get_user_input().split())

                    print_response(Fore.BLUE + "Введіть координати точки C через пробіл: " + Fore.RESET)
                    x3, y3 = map(float, get_user_input().split())

                    a = np.array([x2 - x1, y2 - y1])
                    b = np.array([x3 - x1, y3 - y1])

                    s = 0.5 * np.abs(np.cross(a, b))

                    print_response(Back.BLUE + Fore.BLACK + f'Площа трикутника дорівнює: {s}' + Back.RESET +
                                   Fore.RESET)
                    break

                except ValueError:
                    print_response("Будь ласка, продовжіть введення даних вживаючи коректний формат значень.")

        elif subtopic_number == '2':
            while True:
                try:
                    print_response("Для початку обчислення площі прямокутника, \n" + Fore.BLUE +
"""введіть значення довжини сторони а: """ + Fore.RESET)
                    A = float(get_user_input())

                    print_response(Fore.BLUE + "Введіть значення довжини сторони b:" + Fore.RESET)
                    B = float(get_user_input())

                    s = A * B

                    print_response(Back.BLUE + Fore.BLACK + f"Площа прямокутника дорівнює: {s}" + Back.RESET +
                                   Fore.RESET)
                    break

                except ValueError:
                    print_response("Будь ласка, продовжіть введення даних вживаючи коректний формат значень.")

        elif subtopic_number == '3':
            while True:
                try:
                    print_response("Для початку виведення н-того числа Фібоначчі, " + Fore.BLUE + "ведіть число n: "
                                   + Fore.RESET)
                    n = int(get_user_input())

                    a, b = 0, 1
                    for i in range(n):
                        a, b = b, a + b

                    print_response(Back.BLUE + Fore.BLACK + f"{n}-те число Фібоначчі дорівнює: {a}" + Back.RESET +
                                   Fore.RESET)
                    break

                except ValueError:
                    print_response("Будь ласка, продовжіть введення даних вживаючи коректний формат значень.")

        elif subtopic_number == '4':
            import math

            print_response(Back.BLUE + Fore.BLACK + f'Число π дорівнює: {math.pi}' + Back.RESET + Fore.RESET)

        else:
            print_response("Будь ласка, вкажіть номер в межах доступних підтем.")
            continue

        print_cont_math()
        break

def print_cont_math():
    print_response('Чи бажаєте Ви продовжити працювати в блоці ' + Fore.BLUE + '"математика"' + Fore.RESET +
                   '?(так/ні)')
    while True:
        user_input = get_user_input().lower()
        if user_input == 'так':
            mathem()
            break

        elif user_input == 'ні':
            print_response("Ви можете задати мені питання з наступних тем: " + Fore.BLUE + f"""
{', '.join(topics_dictionary.keys())}.""")
            break

        else:
            print_response(
                'Будь ласка, дайте відповідь у форматі: ' + Fore.RED + '"так" ' + Fore.RESET + 'або ' + Fore.RESET +
                Fore.RED + '"ні".' + Fore.RESET)
            continue


def physics():
        subtopics = topics_dictionary['фізика']

        output = ""
        for i in range(len(subtopics)):
            output += (str(i + 1) + ". " + subtopics[i] + "\n")

        print_response(f'Ви прицюєте в блоці: ' + Fore.BLUE + '"фізика"' + Fore.RESET + '.\n' + Fore.RED +
f'!' + Fore.RESET + 'при необхідності, Ви можете скористатися функціями: "допомога", "назад" та "вихід"'+ Fore.RED +'!\n'
                       + Fore.BLUE +f'Список доступних тем:\n'+ Fore.RESET +
                       f'{output}'
                       f'Введи номер однієї з підтем, допомога з якою тобі потрібна: ')

        while True:
            subtopic_number = get_user_input()
            topic_history_global.append(f"[User]: {subtopic_number}")

            if subtopic_number == 'допомога':
                print_help()
                break

            if subtopic_number == 'назад':
                print_response("Ви можете задати мені питання з наступних тем: " + Fore.BLUE + f"""
{', '.join(topics_dictionary.keys())}.""")
                break

            if subtopic_number == 'вихід':
                print_exit()

            if subtopic_number == '1':
                while True:
                    try:
                        print_response("Для початку обчислення, " + Fore.BLUE + "введіть значення кінетичної енергії: "
                                       + Fore.RESET)
                        E_kin = float(get_user_input())
                        print_response(Fore.BLUE + "Введіть значення потенціальної енергії: "+ Fore.RESET)
                        E_pot = float(get_user_input())
                        print_response(Fore.BLUE + "Введіть значення внутрішньої енергії: "+ Fore.RESET)
                        E_vnutr = float(get_user_input())

                        const = E_kin + E_pot + E_vnutr

                        print_response(Back.BLUE + Fore.BLACK + f"Значення константи дорівнює: {const}" + Back.RESET +
                                       Fore.RESET)
                        break

                    except ValueError:
                        print_response("Будь ласка, продовжіть введення даних вживаючи коректний формат значень.")

            elif subtopic_number == '2':
                h = 6.62607015 * 10 ** - 34
                print_response(Back.BLUE + Fore.BLACK + f"Стала Планка дорівнює: {h} м˄2 * кг/с." + Back.RESET +
                                       Fore.RESET)

            elif subtopic_number == '3':
                k = 8.9875517923 * 10 ** 9
                print_response(Back.BLUE + Fore.BLACK + f"Кулонівська стала дорівнює: {k}" + Back.RESET + Fore.RESET)

            else:
                print_response("Будь ласка, вкажіть номер в межах доступних підтем.")
                continue

            print_cont_physics()
            break

def print_cont_physics():
    print_response('Чи бажаєте Ви продовжити працювати в блоці ' + Fore.BLUE + '"фізика"' + Fore.RESET +
                   '?(так/ні)')
    while True:
        user_input = get_user_input().lower()
        if user_input == 'так':
            physics()
            break

        elif user_input == 'ні':
            print_response("Ви можете задати мені питання з наступних тем: " + Fore.BLUE + f"""
{', '.join(topics_dictionary.keys())}.""")
            break

        else:
            print_response(
                'Будь ласка, дайте відповідь у форматі: ' + Fore.RED + '"так" ' + Fore.RESET + 'або ' + Fore.RESET +
                Fore.RED + '"ні".' + Fore.RESET)
            continue


def geography():
        subtopics = topics_dictionary['географія']

        output = ""
        for i in range(len(subtopics)):
            output += (str(i + 1) + ". " + subtopics[i] + "\n")

        print_response(f'Ви прицюєте в блоці: ' + Fore.BLUE + '"географія"' + Fore.RESET + '.\n' + Fore.RED +
f'!' + Fore.RESET + 'при необхідності, Ви можете скористатися функціями: "допомога", "назад" та "вихід"' + Fore.RED + '!\n'
                       + Fore.BLUE + f'Список доступних підтем:\n' + Fore.RESET +
                       f'{output}'
                       f'Введи номер однієї з підтем, допомога з якою тобі потрібна: ')

        while True:
            subtopic_number = get_user_input()
            topic_history_global.append(f"[User]: {subtopic_number}")

            if subtopic_number == 'допомога':
                print_help()
                break

            if subtopic_number == 'назад':
                print_response("Ви можете задати мені питання з наступних тем: " + Fore.BLUE + f"""
{', '.join(topics_dictionary.keys())}.""")
                break

            if subtopic_number == 'вихід':
                print_exit()

            if subtopic_number == '1':
                print_response(Back.BLUE + Fore.BLACK + "Сахара - це найбільша пустеля в світі, розташована в "
                                                        "Північній Африці." + Back.RESET + Fore.BLUE + f"""
Вона простягається на площі більше + Fore.BLUE + 9 мільйонів квадратних кілометрів і охоплює 
території 10 країн, включаючи Алжир, Чад, Єгипет, Лівію, Малі, Мавританію, Марокко, 
Нігер, Західну Сахару та Судан.""" + Fore.RESET)

            elif subtopic_number == '2':
                print_response(Fore.BLUE + f"""Дві держави, які мають найбільшу кількість кордонів з іншими державами 
- це """ + Back.BLUE + Fore.BLACK + "росія та Китай"+Back.RESET+Fore.BLUE+". росія має кордон з 16 країнами: "
                                                                          "Норвегією, Фінляндією,\n"
f"""Естонією, Латвією, Литвою, Польщею, Білоруссю, Україною, Грузією, Азербайджаном, 
Казахстаном, Монголією, КНР, КНДР, і з Японією через його контрольовані території.
 Китай має кордон з 14 країнами: Афганістаном, Бутаном, Індією, Казахстаном, 
Киргизстаном, Лаосом, М'янмою, Монголією, Непалом, Пакистаном, росією, Таджикистаном, 
В'єтнамом та КНДР.
 Важливо зазначити, що деякі країни можуть мати більше кордонів, ніж росія і Китай, 
якщо враховувати окремі автономні регіони та залежні території, але якщо брати до 
уваги тільки територію держави, то росія та Китай є лідерами з кількості кордонів з 
іншими державами.""" + Fore.RESET)

            elif subtopic_number == '3':
                while True:
                    try:
                        print_response("Для початку обчислення, введіть координату " + Fore.BLUE + "x1: " + Fore.RESET)
                        x1 = float(get_user_input())
                        print_response("Введіть координату " + Fore.BLUE + "y1: " + Fore.RESET)
                        y1 = float(get_user_input())
                        print_response("Введіть координату " + Fore.BLUE + "x2: " + Fore.RESET)
                        x2 = float(get_user_input())
                        print_response("Введіть координату " + Fore.BLUE + "y2: " + Fore.RESET)
                        y2 = float(get_user_input())

                        distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
                        rounded_distance = round(distance, 2)

                        print_response(Back.BLUE + Fore.BLACK + f"Відстань між точками А({x1}, {y1}) та В({x2}, {y2}) "
                                                            f"дорівнює: {rounded_distance}" + Back.RESET + Fore.RESET)
                        break

                    except ValueError:
                        print_response("Будь ласка, продовжіть введення даних вживаючи коректний формат значень.")

            elif subtopic_number == '4':
                while True:
                    try:
                        import math

                        print_response("Для початку обчислення, введіть координату " + Fore.BLUE + "x1: " + Fore.RESET)
                        x1 = float(get_user_input())
                        print_response("Введіть координату " + Fore.BLUE + "y1: " + Fore.RESET)
                        y1 = float(get_user_input())
                        print_response("Введіть координату " + Fore.BLUE + "x2: " + Fore.RESET)
                        x2 = float(get_user_input())
                        print_response("Введіть координату " + Fore.BLUE + "y2: " + Fore.RESET)
                        y2 = float(get_user_input())

                        azimuth = math.atan2(y2 - y1, x2 - x1)
                        degrees = math.degrees(azimuth)
                        rounded_degrees = round(degrees, 2)

                        print_response(Back.BLUE + Fore.BLACK + f"Азимут від точки А({x1}, {y1}) до точки "
                                       f"В({x2}, {y2}) дорівнює {rounded_degrees} градусів" + Back.RESET + Fore.RESET)
                        break

                    except ValueError:
                        print_response("Будь ласка, продовжіть введення даних вживаючи коректний формат значень.")

            else:
                print_response("Будь ласка, вкажіть номер в межах доступних підтем.")
                continue

            print_cont_geography()
            break

def print_cont_geography():
    print_response('Чи бажаєте Ви продовжити працювати в блоці ' + Fore.BLUE + '"географія"' + Fore.RESET +
                   '?(так/ні)')
    while True:
        user_input = get_user_input().lower()
        if user_input == 'так':
            geography()
            break

        elif user_input == 'ні':
            print_response("Ви можете задати мені питання з наступних тем: " + Fore.BLUE + f"""
{', '.join(topics_dictionary.keys())}.""")
            break

        else:
            print_response(
                'Будь ласка, дайте відповідь у форматі: ' + Fore.RED + '"так" ' + Fore.RESET + 'або ' + Fore.RESET +
                Fore.RED + '"ні".' + Fore.RESET)
            continue


def philology():
        subtopics = topics_dictionary['філологія']

        output = ""
        for i in range(len(subtopics)):
            output += (str(i + 1) + ". " + subtopics[i] + "\n")

        print_response(f'Ви прицюєте в блоці: ' + Fore.BLUE + '"філологія"' + Fore.RESET + '.\n' + Fore.RED +
f'!' + Fore.RESET + 'при необхідності, Ви можете скористатися функціями: "допомога", "назад" та "вихід"' + Fore.RED + '!\n'
                       + Fore.BLUE + f'Список доступних підтем:\n' + Fore.RESET +
                       f'{output}'
                       f'Введи номер однієї з підтем, допомога з якою тобі потрібна: ')

        while True:

            subtopic_number = get_user_input()
            topic_history_global.append(f"[User]: {subtopic_number}")

            if subtopic_number == 'допомога':
                print_help()
                break

            if subtopic_number == 'назад':
                print_response("Ви можете задати мені питання з наступних тем: " + Fore.BLUE + f"""
{', '.join(topics_dictionary.keys())}.""")
                break

            if subtopic_number == 'вихід':
                print_exit()

            if subtopic_number == '1':
                import numpy as np

            if subtopic_number == '1':
                print_response(Fore.BLUE + "Іменник і прикметник - це дві різні частини мови, які використовуються "
                                           "для опису\n" 
"різних аспектів об'єктів або понять.\n" +
Back.BLUE + Fore.BLACK + "Іменник" + Back.RESET
          + Fore.BLUE +f""" - це частина мови, що позначає назву людини, тварини, речі, тощо. 
Іменники можуть бути конкретними або абстрактними. Іменники можуть використовуватися 
в ролі суб'єкта або об'єкта речення\n""" +
Back.BLUE + Fore.BLACK + "Прикметник" + Back.RESET
          + Fore.BLUE +f""" - це частина мови, що характеризує іменник або займенник і вказує на його 
ознаки, властивості або стан. Прикметники можуть бути як розряду якісні, так і розряду 
відносні. Прикметники можуть вживатися перед іменниками, або після деяких дієслів, 
таких як "бути", "здаватися", "становити", тощо.\n""" +
 Back.BLUE + Fore.BLACK + "Отже, основна різниця між іменником і прикметником полягає в тому, що іменник позначає"
                        + Back.RESET + Fore.RESET +"\n" +
Back.BLUE + Fore.BLACK +"назву об'єкта або поняття, тоді як прикметник описує його характеристики."
                       + Back.RESET + Fore.RESET)

            elif subtopic_number == '2':
                print_response(Fore.BLUE + "В українській мові налічують сім відмінків:" + Back.BLUE + Fore.BLACK +
                                           "називний, родовий, " + Back.RESET + "\n" +
Back.BLUE + "давальний, знахідний, орудний, місцевий і кличний." + Back.RESET + Fore.BLUE +
f"""\n Змінюються за відмінками ті частини мови, що прийнято звати іменами — іменники, 
прикметники, числівники, а також дієприкметники і займенники.""")

                print_response("Надати визначення кожного з відмінків української мови?(так/ні)")

                while True:
                    user_input = get_user_input().lower()

                    if user_input == 'так':
                        print_response(Back.BLUE + Fore.BLACK + "-Називний відмінок" + Back.RESET + Fore.BLUE +
                                       " відповідає на запитання «хто?», «що?».\n"
"Вважається основним відмінком, від якого утворюють інші.\n"
+ Back.BLUE + Fore.BLACK + "-Родовий відмінок " + Back.RESET + Fore.BLUE +
" відповідає на запитання «хто?», «що?».\n"
"Виражає різновиди означальних відношень.\n"
+ Back.BLUE + Fore.BLACK + "-Давальний відмінок" + Back.RESET + Fore.BLUE +
" відповідає на запитання «кому?», «чому?».\n"
"Позначає роль отримувача чого-небудь внаслідок дії суб'єкта.\n"
+ Back.BLUE + Fore.BLACK + "-Знахідний відмінок" + Back.RESET + Fore.BLUE +
" відповідає на запитання «кого?», «що?».\n"
"Виражає об'єкт, що зазнає прямої дії з боку суб'єкта.\n"
+ Back.BLUE + Fore.BLACK + "-Орудний відмінок" + Back.RESET + Fore.BLUE +
" відповідає на запитання «ким?», «чим?».\n"
"Означає засіб, інструмент, яким виконують дію.\n"
+ Back.BLUE + Fore.BLACK + "-Місцевий відмінок" + Back.RESET + Fore.BLUE +
" відповідає на питання «На/у кому?», «На/у чому?».\n"
"Відмінок, чиїм основним значенням є вираження місця та часу дії.\n"
+ Back.BLUE + Fore.BLACK + "-Кличний відмінок" + Back.RESET + Fore.BLUE +
" позначає звертання до певної особи чи предмета.\n" 
"Посилює стилістичні функції звертань.")
                        break

                    elif user_input == 'ні':
                        break

                    else:
                        print_response(
                            'Будь ласка, дайте відповідь у форматі: ' + Fore.RED + '"так" ' + Fore.RESET + 'або '
                            + Fore.RESET + Fore.RED + '"ні".' + Fore.RESET)
                        continue

            else:
                print_response("Будь ласка, вкажіть номер в межах доступних підтем.")
                continue

            print_cont_philology()
            break

def print_cont_philology():
    print_response('Чи бажаєте Ви продовжити працювати в блоці ' + Fore.BLUE + '"філологія"' + Fore.RESET +
                   '?(так/ні)')
    while True:
        user_input = get_user_input().lower()
        if user_input == 'так':
            philology()
            break

        elif user_input == 'ні':
            print_response("Ви можете задати мені питання з наступних тем: " + Fore.BLUE + f"""
{', '.join(topics_dictionary.keys())}.""")
            break

        else:
            print_response(
                'Будь ласка, дайте відповідь у форматі: ' + Fore.RED + '"так" ' + Fore.RESET + 'або ' + Fore.RESET +
                Fore.RED + '"ні".' + Fore.RESET)
            continue


def astronomy():
        subtopics = topics_dictionary['астрономія']

        output = ""
        for i in range(len(subtopics)):
            output += (str(i + 1) + ". " + subtopics[i] + "\n")

        print_response(f'Ви прицюєте в блоці: ' + Fore.BLUE + '"астрономія"' + Fore.RESET + '.\n' + Fore.RED +
f'!' + Fore.RESET + 'при необхідності, Ви можете скористатися функціями: "допомога", "назад" та "вихід"' + Fore.RED + '!\n'
                       + Fore.BLUE + f'Список доступних підтем:\n' + Fore.RESET +
                       f'{output}'
                       f'Введи номер однієї з підтем, допомога з якою тобі потрібна: ')

        while True:

            subtopic_number = get_user_input()
            topic_history_global.append(f"[User]: {subtopic_number}")

            if subtopic_number == 'допомога':
                print_help()
                break

            if subtopic_number == 'назад':
                print_response("Ви можете задати мені питання з наступних тем: " + Fore.BLUE + f"""
{', '.join(topics_dictionary.keys())}.""")
                break

            if subtopic_number == 'вихід':
                print_exit()

            if subtopic_number == '1':
                import numpy as np

            if subtopic_number == '1':
                print_response(Back.BLUE + Fore.BLACK + "У астрономії відомо багато типів зір, але основними з них "
                                                        "є на наступні категорії:" + Back.RESET + Fore.BLUE +
f"""\nНейтронна зірка(найменший тип зірок у Всесвіті), Червоні карлики(мала й відносно 
холодна зоря головної послідовності), Помаранчевий карлик(що знаходиться посередині 
між червоним карликом та жовтим карликом), Жовті карлики(тип невеликих зір(маси Сонця)), 
Білий карлик(зорі низької світності з масами, порівняними із масою Сонця),
Бурий карлик(самосвітний астрономічний об'єкт), Синій карлик(гіпотетичний тип зірок),
Чорний карлик(білі карлики, які охололи і майже не випромінюють у видимому діапазоні),
Підкарлик(тип зірок, що знаходиться на півдорозі між "справжньою" зіркою та 
коричневим карликом), Субгігант(зірка, яскравіша за звичайну зірку головної 
послідовності), Гігантська зірка(тип зірок з діаметр у 10-100 разів більший за Сонце),
Світловий гігант(тип зірки, що знаходиться на півдорозі між гігантською зіркою та 
надгігантом), Супергіганти(зірки, які мають діаметр приблизно в 500 разів більший за 
Сонце), Світловий надгігант(на півдорозі між надгігантом і гіпергігантом),
Гіпергігант(найпотужніші, найважчі, найяскравіші, найрідкісніші надгіганти.""")

            elif subtopic_number == '2':
                print_response(Back.BLUE + Fore.BLACK + "Найбільшою орбітою в Сонячній системі володіє Нептун, "
                                                        "а найменшою - Меркурій." + Back.RESET + Fore.BLUE +
f"""\n Орбіта Нептуна має середню відстань від Сонця близько 4,5 мільярдів кілометрів, що 
є більшою, ніж відстань між Землею та Сонцем в 30 разів.
 Меркурій має найменшу орбіту серед планет Сонячної системи. Його середня відстань 
від Сонця становить близько 58 мільйонів кілометрів, що менше відстані між Землею та 
Сонцем більш ніж в 3,7 раза.""")

            else:
                print_response("Будь ласка, вкажіть номер в межах доступних підтем.")
                continue

            print_cont_astronomy()
            break

def print_cont_astronomy():
    print_response('Чи бажаєте Ви продовжити працювати в блоці ' + Fore.BLUE + '"астрономія"' + Fore.RESET +
                   '?(так/ні)')
    while True:
        user_input = get_user_input().lower()
        if user_input == 'так':
            astronomy()
            break

        elif user_input == 'ні':
            print_response("Ви можете задати мені питання з наступних тем: " + Fore.BLUE + f"""
{', '.join(topics_dictionary.keys())}.""")
            break

        else:
            print_response(
                'Будь ласка, дайте відповідь у форматі: ' + Fore.RED + '"так" ' + Fore.RESET + 'або ' + Fore.RESET +
                Fore.RED + '"ні".' + Fore.RESET)
            continue


def general_questions():
        subtopics = topics_dictionary['загальні запитання']

        output = ""
        for i in range(len(subtopics)):
            output += (str(i + 1) + ". " + subtopics[i] + "\n")

        print_response(f'Ви прицюєте в блоці: ' + Fore.BLUE + '"загальні запитання"' + Fore.RESET + '.\n' + Fore.RED +
f'!' + Fore.RESET + 'при необхідності, Ви можете скористатися функціями: "допомога", "назад" та "вихід"' + Fore.RED + '!\n'
                       + Fore.BLUE + f'Список доступних підтем:\n' + Fore.RESET +
                       f'{output}'
                       f'Введи номер однієї з підтем, допомога з якою тобі потрібна: ')

        while True:
            import datetime
            import random

            subtopic_number = get_user_input()
            topic_history_global.append(f"[User]: {subtopic_number}")

            if subtopic_number == 'допомога':
                print_help()
                break

            if subtopic_number == 'назад':
                print_response("Ви можете задати мені питання з наступних тем: " + Fore.BLUE + f"""
{', '.join(topics_dictionary.keys())}.""")
                break

            if subtopic_number == 'вихід':
                print_exit()

            if subtopic_number == '1':
                import datetime
                now = datetime.datetime.now()
                time = now.strftime("%H:%M:%S")
                print_response(Back.BLUE + Fore.BLACK + f"Поточний час: {time}." + Back.RESET + Fore.RESET)

            elif subtopic_number == '2':
                month = {"January": "січень",
                         "February": "лютий",
                         "March": "березень",
                         "April": "квітень",
                         "May": "травень",
                         "June": "червень",
                         "July": "липень",
                         "August": "серпень",
                         "September": "вересень",
                         "October": "жовтень",
                         "November": "листопад",
                         "December": "грудень"}

                now = datetime.datetime.now()
                month_en = now.strftime("%B")
                month_ua = month[month_en]
                print_response(Back.BLUE + Fore.BLACK + f"Поточний місяць: {month_ua}." + Back.RESET + Fore.RESET)

            elif subtopic_number == '3':
                now = datetime.datetime.now()
                year = now.year
                print_response(Back.BLUE + Fore.BLACK + f"Поточний рік: {year}." + Back.RESET + Fore.RESET)

            elif subtopic_number == '4':
                season_names = {"winter": "зима",
                                "spring": "весна",
                                "summer": "літо",
                                "autumn": "осінь"}

                now = datetime.datetime.now()
                month = now.month
                if month in [1, 2, 12]:
                    season = "winter"
                elif month in [3, 4, 5]:
                    season = "spring"
                elif month in [6, 7, 8]:
                    season = "summer"
                else:
                    season = "autumn"

                season_ua = season_names[season]
                print_response(Back.BLUE + Fore.BLACK + f"Поточна пора року: {season_ua}." + Back.RESET + Fore.RESET)

            elif subtopic_number == '5':
                today = datetime.date.today()
                new_year = datetime.date(today.year, 12, 31)
                days_left = (new_year - today).days
                print_response(Back.BLUE + Fore.BLACK + f"До Нового Року залишилось {days_left} днів."
                               + Back.RESET + Fore.RESET)

            elif subtopic_number == '6':

                options = ["камінь", "ножиці", "папір"]

                bot_choice = random.choice(options)

                print_response(Fore.BLUE + "Введіть: камінь, ножиці або папір: " + Fore.RESET)
                user_choice = get_user_input().lower()

                while user_choice not in options:
                    print_response("Невірний формат введених даних. Спробуйте ще раз.\n"
                     + Fore.BLUE + "Введіть: камінь, ножиці або папір:")
                    user_choice = get_user_input().lower()
                    continue

                if user_choice == bot_choice:
                    print_response(Back.BLUE + Fore.BLACK + f"Нічия! Я також обрав {bot_choice}." + Back.RESET
                                   + Fore.RESET)
                elif user_choice == "камінь" and bot_choice == "ножиці":
                    print_response(Back.BLUE + Fore.BLACK + "Ви перемогли! Я обрав ножиці." + Back.RESET + Fore.RESET)

                elif user_choice == "ножиці" and bot_choice == "папір":
                    print_response(Back.BLUE + Fore.BLACK + "Ви перемогли! Я обрав папір." + Back.RESET + Fore.RESET)

                elif user_choice == "папір" and bot_choice == "камінь":
                    print_response(Back.BLUE + Fore.BLACK + "Ви перемогли! Я обрав камінь." + Back.RESET + Fore.RESET)

                else:
                    print_response(Back.BLUE + Fore.BLACK + f"Ви програли! Я обрав {bot_choice}." + Back.RESET
                                   + Fore.RESET)

            elif subtopic_number == '7':

                print_response(Fore.BLUE + "Мене звати " + Back.BLUE + Fore.BLACK + "Нані" + Back.RESET
                               + Fore.BLUE + ". А тебе як?" + Fore.RESET)
                user_name = get_user_input()

                print_response(Fore.BLUE + "Приємно познайомитись, " + Back.BLUE + Fore.BLACK + f"{user_name}"
                               + Back.RESET + Fore.BLUE + "!" + Fore.RESET)

            elif subtopic_number == '8':

                carols = [Back.BLUE + Fore.BLACK + '"Добрий вечір тобі, пане господарю"' + Back.RESET + Fore.BLUE +

f"""\nДобрий вечір тобі, пане господарю, радуйся!
Ой радуйся, земле, Син Божий народився!

Застеляйте столи, та все килимами, радуйся!
Ой радуйся, земле, Син Божий народився!

Та кладіть калачі з ярої пшениці, радуйся!
Ой радуйся, земле, Син Божий народився!

Бо прийдуть до тебе три празники в гості, радуйся!
Ой радуйся, земле, Син Божий народився!""",
Back.BLUE + Fore.BLACK + '"Нова радість стала"' + Back.RESET + Fore.BLUE +

f"""\nНова радість стала, яка не бувала,
Над вертепом звізда ясна світлом засіяла.

Де Христос родився, з Діви воплотився,
Як чоловік пеленами убого оповився.

Пастушки з ягнятком перед тим дитятком
На колінця припадають, Царя-Бога вихваляють.""",
Back.BLUE + Fore.BLACK + '"Бог предвічний"' + Back.RESET + Fore.BLUE +

f"""\nБог предвічний народився,
Прийшов днесь із небес,
Щоб спасти люд свій весь,
І утішився.

В Вифлеємі народився,
Месія, Христос наш,
І пан наш, для всіх нас,
Нам народився.""",
Back.BLUE + Fore.BLACK + '"Во Вифлиємі нині новина"' + Back.RESET + Fore.BLUE +

f"""\nВо Вифлеємі нині новина:
Пречиста Діва зродила Сина,
В яслах сповитий поміж бидляти,
Спочив на сіні Бог необнятий.

Вже Херувими славу співають,
Ангельські хори Пана витають,
Пастир убогий несе, що може,
Щоб подарити Дитятко Боже.""",
Back.BLUE + Fore.BLACK + '"Бог ся рождає"' + Back.RESET + Fore.BLUE +

f"""\nТут Ангели чудяться,
Рожденного бояться,
А віл стоїть, трясеться,
Осел смутно пасеться.
Пастиріє клячуть,
В плоти Бога бачуть,
Тут же, тут же,
Тут же, тут же, тут!"""]

                selected_carols = random.choice(carols)

                print_response(f'Чудовий вибір! Я знаю цілих 5 колядок.\n'
                               f'Ось одна з них:\n'
                               f'{selected_carols}')

            elif subtopic_number == '9':

                quote = [Back.BLUE + Fore.BLACK + "«Успіх — це вміння рухатись від невдачі до невдачі, не втрачаючи "
                                                  "ентузіазму»"  + Back.RESET + Fore.BLUE +
"\n— Вінстон Черчилль.",
Back.BLUE + Fore.BLACK + "«Ти повинен займатися тим, що робить тебе щасливим. Забудь про гроші або" + Back.RESET +
"\n" + Back.BLUE + "інші пастки, які заведено вважати успіхом. У тебе всього одне життя»" + Back.RESET + Fore.BLUE +
"\n— Карл Лагерфельд.",
Back.BLUE + Fore.BLACK + "«Поки ми живі, ми повинні виконувати свої обіцянки, хоч які б складні вони не були»"
+ Back.RESET + Fore.BLUE +
"\n— Філіп Пуллман.",
Back.BLUE + Fore.BLACK + "«Я краще найняв би людину з ентузіазмом, аніж людину, яка все знає»"+ Back.RESET + Fore.BLUE +
"\n— Джон Девісон Рокфеллер.",
Back.BLUE + Fore.BLACK + "«Зміни — закон життя. І ті, хто дивиться тільки в минуле чи лише на сьогодення," + Back.RESET+
"\n" + Back.BLUE + "пропустять майбутнє»" + Back.RESET + Fore.BLUE +
"\n— Джон Ф. Кеннеді."]

                selected_quote = random.choice(quote)

                print_response(f'Чудовий вибір! Я знаю цілих 5 мотивуючих цитат.\n'
                               f'Ось одна з них:\n'
                               f'{selected_quote}')

            elif subtopic_number == '10':

                joke = [Back.BLUE + Fore.BLACK + f"Операційна. Медсестра кричить:" + Back.RESET +
"\n" + Back.BLUE + "– У нього з’явився пульс, він повертається!" + Back.RESET +
"\n" + Back.BLUE + "Тут лікар вирубає електрику:" + Back.RESET +
"\n" + Back.BLUE + "– Повертатися – погана прикмета." + Back.RESET,
Back.BLUE + Fore.BLACK + f"Почувши мої бажання, Золота рибка зробила вигляд, що здохла." + Back.RESET,
Back.BLUE + Fore.BLACK + "Що поєднує викладача фізичної культури та гопника?" + Back.RESET +
"\n" + Back.BLUE + "Віджимання." + Back.RESET,
Back.BLUE + Fore.BLACK + "Чому охоронці ринку завжди ввічливі?" + Back.RESET +
"\n" + Back.BLUE + "Вони слідкують за базаром." + Back.RESET,
Back.BLUE + Fore.BLACK + "Ніколи не смійся з цигана, що їде на велосипеді." + Back.RESET +
"\n" + Back.BLUE + "Це може бути твій велосипед." + Back.RESET]

                selected_joke = random.choice(joke)

                print_response(f'Чудовий вибір! Я знаю цілих 5 анекдотів.\n'
                               f'Ось один з них:\n'
                               f'{selected_joke}')

            else:
                print_response("Будь ласка, вкажіть номер в межах доступних підтем.")
                continue

            print_cont_general_questions()
            break

def print_cont_general_questions():
    print_response('Чи бажаєте Ви продовжити працювати в блоці ' + Fore.BLUE + '"загальні запитання"' + Fore.RESET +
                   '?(так/ні)')
    while True:
        user_input = get_user_input().lower()
        if user_input == 'так':
            general_questions()
            break

        elif user_input == 'ні':
            print_response("Ви можете задати мені питання з наступних тем: " + Fore.BLUE + f"""
{', '.join(topics_dictionary.keys())}.""")
            break

        else:
            print_response(
                'Будь ласка, дайте відповідь у форматі: ' + Fore.RED + '"так" ' + Fore.RESET + 'або ' + Fore.RESET +
                Fore.RED + '"ні".' + Fore.RESET)
            continue


import sys
def print_exit():
    print_response('Радий був поспілкуватися. Бувайте!' + Fore.RED + '❤')
    with open(f"dialog-{datetime.now().strftime(r'%d-%m-%Y--%H-%M-%S')}.txt", "w", encoding="utf-8") as f1:
        for line in topic_history_global:
            f1.write(line)
            f1.write("\n")
    sys.exit()


def print_greeting():
    global topics_dictionary
    greeting = "Привіт! Мене звати Нані. Ви можете задати мені питання з наступних тем: " + Fore.BLUE + f"""
{', '.join(topics_dictionary.keys())}."""
    print_response(greeting)


def print_response(text):
    response = (Fore.LIGHTBLUE_EX + f'[Bot]' + Fore.RESET + f': {text}')
    print(response)
    response = response.replace("", "")
    response = re.sub(r"\[(\d+)m", "", response)

    topic_history_global.append(response)


def get_user_input():
    return input(Fore.GREEN + '[User]: ')


def print_help():
    help_message = ""
    if len(topic_history_user) == 0:
        help_message += "Для подальшого вирішення проблеми, введіть назву операції:"
    else:
        help_message += f"Ви обрали операцію" + Fore.BLUE + "«{get_current_topic()}»" + Fore.RESET

    help_message += f"\nДля виходу, напишіть " + Fore.BLUE + "«вихід»" + Fore.RESET + \
                    ".\nДля повернення на початок, напишіть " + Fore.BLUE + "«назад»." + Fore.RESET
    print_response(help_message)


def get_current_topic():
    global topic_history_user
    if len(topic_history_user) == 0:
        return None
    return topic_history_user[-1]


print_greeting()

while True:
    try:
        input_text = get_user_input()
        topic_history_global.append(f"[User]: {input_text}")
    except KeyboardInterrupt:
        break

    if input_text.lower() == 'вихід':
        break

    if input_text.lower() == 'допомога':
        print_help()
        continue

    if input_text.lower() == 'назад':
        print_greeting()
        continue

    if input_text.lower() == 'математика':
        mathem()
        continue

    if input_text.lower() == 'фізика':
        physics()
        continue

    if input_text.lower() == 'географія':
        geography()
        continue

    if input_text.lower() == 'філологія':
        philology()
        continue

    if input_text.lower() == 'астрономія':
        astronomy()
        continue

    if input_text.lower() == 'загальні запитання':
        general_questions()
        continue

    else:
        if input_text.lower() in topics_dictionary:
            topic_history_user.append(input_text)
        else:
            print_response('Я не знаю цієї теми. Спробуй ще раз.')
            continue

print_response('Радий був поспілкуватися. Бувайте!' + Fore.RED + '❤')

with open(f"dialog-{datetime.now().strftime(r'%d-%m-%Y--%H-%M-%S')}.txt", "w", encoding="utf-8") as f1:
    for line in topic_history_global:
        f1.write(line)
        f1.write("\n")