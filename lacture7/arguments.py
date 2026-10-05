def average(a , b):
    print("The average is :", (a+b) / 2)

average(5 , 10)

#1 Default argument

def name(fname,sname,pname,rname):
    print("Hello",fname, pname,rname,sname)

name("Rahul","Raj", "prince","Gulshan")

#keyword Arguments

def plus(a , b):
    print("sum is ", a+ b)

plus(b = 8, a =6)

#order matter nhi karta hai phale b aya ya a koi faraf nhi padta 

#3 Required arguments
def plus(a , b):
    print("sum is ", a+ b)

plus(b = 8, a = 53)

#A and B ki value dani he padagi