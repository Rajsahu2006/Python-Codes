n = int(input("Enter the input"))
even = 0
odd = 0
for i in range (1,n+1):
    if n%i ==0:
        print(i,end="")
        if i%2==0:
            even += 1

        else:
            odd += 1

print("odd factors are", odd,"Even factor are even",even)

