def even_fact(n):
    ans =1
    for i in range(1,1+n):
        ans *= i
        return ans
def odd_fact(n):
    ans = 1
    for i in range(1,1+n,2):
        ans *= i
        return ans
n = int(input("Enter the number:"))
if n%2 == 0:
    print(odd_fact(n))
else:
    print(even_fact(n))