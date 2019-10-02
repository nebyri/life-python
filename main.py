from time import sleep
from random import randint

k = 100
world = []
era = 0

# создаём наш мир заполненный рандомно 1 - рыбла, 2 - креветка, 3 - камень (я не дам)
for line in range(k):
    line = []
    for index in range(k):
        cell = [randint(0, 3), 0]
        line.append(cell)
    world.append(line)


class bcolors:
    OKRED = '\033[31m'
    OKBLUE = '\033[36m'
    OKGREY = '\033[37m'
    ENDC = '\033[0m'

def print_lines():  # функция, выводящая состояние поля в удобном виде
    print ("World")
    for i in range(k):
        for j in range(k):
            print(bcolors.OKBLUE + '@'+ bcolors.ENDC if world[i][j][0]==1 else bcolors.OKGREY+'#'+ bcolors.ENDC if world[i][j][0]==3 else bcolors.OKRED + '^'+ bcolors.ENDC if world[i][j][0]==2 else " ", end=" ")
        print()
    print()




# обновляем "теневую" часть мира
def counter():
    for i in range(k):
        for j in range(k):  # перебираем все клетки

            x_from, y_from = i - 1, j - 1
            x_to, y_to = i + 1, j + 1

            if x_from < 0:  # дальнейшие 8 строчек нужны, дабы не сослаться на элементы, выходящие за пределы массива
                x_from = 0

            if y_from < 0:
                y_from = 0

            if x_to > k - 1:
                x_to = k - 1

            if y_to > k - 1:
                y_to = k - 1

            summ = 0
            if world[i][j][0] == 1:
                for x in range(x_from, x_to + 1):
                    for y in range(y_from, y_to + 1):  # перебираем квадрат 3*3 и считаем сколько там "живых" клеток
                        if world[x][y][0] == 1:
                           summ += 1
                summ -= 1  # вычитаем из суммы еденицу чтобы не считать "видимое" существо
                world[i][j][1] = summ  # добавляем в "третье" измерение кол-во соседей
            summ = 0
            if world[i][j][0] == 2:
                for x in range(x_from, x_to + 1):
                    for y in range(y_from, y_to + 1):  # перебираем квадрат 3*3 и считаем сколько там "живых" клеток
                        if world[x][y][0] == 2:
                           summ += 1
                summ -= 1 # вычитаем из суммы еденицу чтобы не считать "видимое" существо
                world[i][j][1] = summ  # добавляем в "третье" измерение кол-во соседей
            sumf = 0 # количество соседей-рыб
            sumk = 0 # количество соседей-креветок
            # ищем соседей у пустых клеток
            if world[i][j][0] == 0:
                for x in range(x_from, x_to + 1):
                    for y in range(y_from, y_to + 1):  # перебираем квадрат 3*3 и считаем сколько там "живых" клеток
                        if world[x][y][0] == 1:
                            sumf += 1
                        if world[x][y][0] == 2:
                            sumk += 1
                if sumf == 3:
                    world[i][j][1] = 1  # добавляем в "третье" измерение кол-во соседей
                else:
                    if sumk == 3:
                        world[i][j][1] = 2  # добавляем в "третье" измерение кол-во соседей


def step():  # пробегаемся по массиву и в зависимости от кол-ва соседей клетки меняем (или не меняем) ее состояние
    for i in range(k):
        for j in range(k):
            if world[i][j][0] == 1:
                if world[i][j][1] == 2 or world[i][j][1] == 3:
                    world[i][j][0] = 1
                else:
                    if world[i][j][1] >= 4 or world[i][j][1] < 2:
                        world[i][j][0] = 0
            else:
                if world[i][j][0] == 2:
                    if world[i][j][1] == 2 or world[i][j][1] == 3:
                        world[i][j][0] = 2
                    else:
                        if world[i][j][1] >= 4 or world[i][j][1] < 2:
                            world[i][j][0] = 0
                else:
                    if world[i][j][0] == 0:
                        if world[i][j][1] == 1 or world[i][j][1] == 2:
                            world[i][j][0] = world[i][j][1]
    print_lines()
    for i in range(k):
        for j in range(k):
            world[i][j][1] = 0
    counter()


def life_counter_f():  # пробегаемся по массиву и суммируем живые клетки (работать будет и без этого)
    f = 0
    for i in range(k):
        for j in range(k):
            if world[i][j][0] == 1:
                f = f + 1
    return f


def life_counter_k():  # пробегаемся по массиву и суммируем живые клетки (работать будет и без этого)
    kr = 0
    for i in range(k):
        for j in range(k):
            if world[i][j][0] == 2:
                kr = kr + 1
    return kr


print_lines()
print("Рыб:", life_counter_f(), "креветок:", life_counter_k(), "эпоха",era)
counter()
while life_counter_f() > 0 or life_counter_k() > 0:  # продолжаем работать с полем, пока есть хоть одна живая клетка
    step()
    era = era + 1
    print("Рыб:", life_counter_f(), "креветок:", life_counter_k(), "эпоха", era)
    sleep(1)
