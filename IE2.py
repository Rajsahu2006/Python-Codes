#Nested if else

a = int(input("Enter your no.  :"))
if(a<0):
    print("no. is nagitive")

elif(a<=10):
    print("no. is 1 - 10")
    if(a<20):
        print("no. is 1 - 20")
    else:
        print("no. is greater then 20")

else:
    print("no. is zero")