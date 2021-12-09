import math

#First_____________________________________________________________
'''Написать скрипт для движения персонажа влево, вправо, вверх и вниз по координатам x и y по координатной оси.
   Начальная позиция персонажа (0;0)
'''
print("Select: up, down, right, left")
move = input()
x = 0
y = 0
if(move == "up"): 
    y += 1
elif(move == "down"): 
    y -= 1
elif(move == "left"): 
    x -= 1
elif(move == "right"): 
    x += 1
else: 
    print("Wrong!!!")
print("Position: ({},{})".format(x, y))
print()

#Second_____________________________________________________________
'''Предыдущее, но скрипт бесконечный (каждый раз спрашивается куда движение и выводится результат). 
   Обязательно стоп-слово.
'''
print("Select: up, down, right, left or stop")
x = 0
y = 0
while True: # Всё повторяется в бесконечном цикле, пока не будет введено стоп-слово
    move = input()
    if(move == "up"): 
        y += 1
    elif(move == "down"): 
        y -= 1
    elif(move == "left"): 
        x -= 1
    elif(move == "right"): 
        x += 1
    elif(move == "stop"): #Стоп-слово
        print()
        break
    else: 
        print("Wrong!!!")
    print("Position: ({},{})".format(x, y))

#Third______________________________________________________
'''Написать скрипт решения квадратного уравнения
'''
print("Enter a, b and c")
a = float(input())
b = float(input())
c = float(input())
if(a == 0): # Обработка исключения: при а = 0 уравнение не квадратное
    print("This is not a quadratic equation!")
else:
    d = b**2 - 4*a*c
    if(d > 0): # Положительный дискриминант - решения два
        print("Two solutions: {} and {}".format((-1*b+math.sqrt(d))/(2*a), (-1*b-math.sqrt(d))/(2*a)))
    elif(d == 0): # Нулевой дискриминант - решение одно
        print("One solution: {}".format((-1*b)/(2*a)))
    else: # Дискриминант меньше нуля - решений у уравненеия нет
        print("The equation has no solution")
print()

#Fourth____________________________________________________________
'''C обработкой отрицательного дискриминанта (с комплексными числами), со случаем, если коэффициенты являются комплексными числами.
'''
print("Enter a, b and c")
a = float(input())
b = float(input())
c = float(input())
if(a == 0):
    print("This is not a quadratic equation!")
else:
    d = b**2 - 4*a*c
    if(d > 0):
        print("Two solutions: {} and {}".format((-1*b + math.sqrt(d)) / (2*a), 
                                                (-1*b - math.sqrt(d)) / (2*a)))
    elif(d == 0):
        print("One solution: {}".format((-1*b) / (2*a)))
    else: # Случай, когда у уравнения отрицательный дискриминант
        d *= -1 # Умножаем отрицательный дисккриминант на -1, чтобы нормально извлечь из него корень
        print("Two solutions: {} and {}".format(complex(-b, math.sqrt(d)) / (2*a), 
                                                complex(-b, -math.sqrt(d)) / (2*a)))