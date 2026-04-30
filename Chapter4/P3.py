n = int (input("Enter the number"))
temp = n
c = 0
while temp >0:
    c +=1
    temp //=10

ans =0
temp = n
while temp >0:
    r = temp%10
    ans = ans + r**c
    temp //=10     

if ans == n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
