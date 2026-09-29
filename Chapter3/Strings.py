#Strings in python
name = "Ommmm"

nameshort = name[0:4] # start from index 0 all the way till 3 (exluding 3)
print(nameshort)
name = "Amazing"
nameshort = name[1:5:4] # start from index 1 all the way till 4 (exluding 5) and take every 3rd character
print(nameshort)

apple = " I am Good "
print("lets use a for loop\n")
for character in apple:
    print(character)

Name = "RajSahu"
print(len(Name))
Nameshort = Name[-3:-1]
print(Nameshort)

#Normal slicing left → right chalti hai. Tum -1 se start kar rahe ho aur -3 par stop kar rahe ho, lekin -1 ke baad normal direction mein -3 nahi aata.