st = set()
st1= {}
print(st)
print(type(st))
print(type(st1))


#Question 2
st ={1,2,3,4,4,5}
for i in st:
    print(i)


#Question 3
st = {1,2,34,5,(35,2,4,5),"Hello",48.8}
st.remove(34)
st.discard(1)
print(st)