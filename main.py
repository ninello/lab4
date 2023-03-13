def num1(num: int):
    return True if num % 3 == 0 else False

def num2(num):
    res = None
    try:
        res = 100 / float(num)
    except ValueError:
        print("В эту функцию нужно передать число")
    except ZeroDivisionError:
        print("Ошибка: деление на ноль")
    except Exception as e:
        print("Ошибка: ", e)
    return res

def num3(date: str):
    try:
        date = date.split(".")
        return True if int(date[0]) * int(date[1]) == int(date[2][2:]) else False
    except:
        print("Функция принимает строку с датой в формате dd.mm.yyyy")

def num4(tick: str):
    sum1 = sum([int(i) for i in tick[:int(len(tick) / 2)]])
    sum2 = sum([int(i) for i in tick[int(len(tick) / 2):]])

    if sum1 == sum2:
        return True
    else:
        return False


if num1 == "main":
    print("Проверка функции деления на три")
    print(num1(14))
    print(num1(15))

    print("\nПроверка функции деления 100 на число")
    print(num1(10))
    print(num1(0))
    print(num1(100))

    print("\nПроверка функции магической даты")
    print(num3("22.01.2022"))
    print(num3("21.01.2022"))

    print("\nПроверка функции счастливого билета")
    print(num4("385916"))
    print(num4("231002"))