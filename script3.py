import math

#First
print("Select: up, down, right, left")
move = input()
x=0
y=0
if(move=="up"): y+=1
elif(move=="down"): y-=1
elif(move=="left"): x-=1
elif(move=="right"): x+=1
else: print("Wrong!!!")
print("Position: ({},{})".format(x, y))
print()

#Second
print("Select: up, down, right, left or stop")
x = 0
y = 0
while True:
    move = input()
    if(move=="up"): y+=1
    elif(move=="down"): y-=1
    elif(move=="left"): x-=1
    elif(move=="right"): x+=1
    elif(move=="stop"): 
        print()
        break
    else: print("Wrong!!!")
    print("Position: ({},{})".format(x, y))

#Third
print("Enter a, b and c")
a=float(input())
b=float(input())
c=float(input())
if(a==0):
    print("This is not a quadratic equation!")
else:
    d=b**2-4*a*c
    if(d>0):
        print("Two solutions: {} and {}".format((-1*b+math.sqrt(d))/(2*a), (-1*b-math.sqrt(d))/(2*a)))
    elif(d==0):
        print("One solution: {}".format((-1*b)/(2*a)))
    else: print("The equation has no solution")
print()


#Fourth
print("Enter a, b and c")
a=float(input())
b=float(input())
c=float(input())
if(a==0):
    print("This is not a quadratic equation!")
else:
    d=b**2-4*a*c
    if(d>0):
        print("Two solutions: {} and {}".format((-1*b+math.sqrt(d))/(2*a), (-1*b-math.sqrt(d))/(2*a)))
    elif(d==0):
        print("One solution: {}".format((-1*b)/(2*a)))
    else:
        d*=-1
        print("Two solutions: {} and {}".format(complex(-b, math.sqrt(d))/(2*a), complex(-b, -math.sqrt(d))/(2*a)))
