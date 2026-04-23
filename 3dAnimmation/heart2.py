import math
from turtle import *
def Hearta(k):
    return 15 * math.sin(k)**3
def Heartb(k):
    return 12 *math.cos(k) - 5 * \
        math.cos(2 *k) -2 *\
        math.cos(3*k) -\
        math.cos(4 *k) 
speed(10)
bgcolor("black")
for i in range(100):
    goto(Hearta(i) * 20,Heartb(i) * 20)
    for j in range (1):
        color("purple")
    dot() #drow a dot at the current possition
goto(0,0)
# heart draw hone ke baad
penup()
goto(0, -20)
color("Red")
write("I Love You ❤️", align="center", font=("Arial", 24, "bold"))

done()
       


        
