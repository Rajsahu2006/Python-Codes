#Good Morning sir

from datetime import datetime  # python ke build in module hai jo data or time ke sath kam karta hai

current_hour = datetime.now().hour #current date + time

if current_hour < 12:
    print("Good Morning Sir")
elif current_hour < 17:
    print("Good Afternoon Sir")
else:
    print("Good Evening Sir")
