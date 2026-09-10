#Match Case stateMent

n = int(input("Enter your marks :"))

match n:
    case _ if n == 32:
        print("Border of the passing marks")

    case _ if n > 50:
        print("Good marks")
    case _ if n > 70:
        print("Excilent")
        
    case _ if n <80:
        print("Brilent A+")
        

    case 5 :
        print("Invalid")
        



