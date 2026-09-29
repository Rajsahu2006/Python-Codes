#Functions in Strigs

#strings is a immutable
name = "ebjhudge"

print(len(name))
print(name.endswith("dge"))
print(name.startswith("ebj"))
print(name.capitalize()) #change first latter of string in uppercase
print(name.upper()) #change uppercase
print(name.lower()) #change lowercase

B = "Brotherss!!!"
print(B.rstrip("!")) #remome explaction mark

print(B.replace("Brotherss","Sisters")) #replace brothers into sisters

a = "raj is a good\
    boy" # \escape sequence character
print(a)
print(a.split(" "))
print(a.find("is"))  #Detact index of character

#center method
z = "Introduction"
print(z.center(50))
print(z.count("t"))