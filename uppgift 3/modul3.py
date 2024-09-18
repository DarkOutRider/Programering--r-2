print("Hello world")
name = input("name: ")
try:
    Age = float(input("Age: "))
except:
    print("write your age in number")
    exit()
print(f"welcome {name} you are {Age} years old")
print("Age:", Age)
age_in_weeks = (int(Age) * int(54))
print("Age in weeks:", age_in_weeks)

try:
    weight = int(input("weight in KG: "))
except:
    print("skriv vikten i nummer")
    exit()
lbs = (int(weight) * float(2.20462262185))
print("pound:", lbs)
length_in_meter = input("lengt in meter:" )
print("weight after the length in kg:",weight / (float(length_in_meter) * float(length_in_meter)) )


balder_online = True

if balder_online:
    try:
        height = float(input("Höjd i meter: "))
    except:
        print("skriv höjd i nummer")
        exit()
    if height >= 1.3 and height <=1.99:
        print("Du kan åka")
    else:
        print("Du kan inte åka")
else:
    print("balder är tyvärr stängd")

r = float(input("hur lång är radien: "))

print("svar: ", r*r*3.14)

import random
attempts = int(input("attemps: "))
count = 0
while count < attempts:
    count += 1
    print(random.randint(1, 6))


