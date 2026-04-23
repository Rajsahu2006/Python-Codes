lst=[8,10,12,13,16,21]
print(lst)
for i in range(len(lst)):
    if lst[i]%2==0:
        lst[i]-=5
    else:
        lst[i]+=5
        print(lst)