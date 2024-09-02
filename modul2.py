

"""
DATATYPER I PYTHON

sträng, string: "text
heltal, integer = 1... 2... 3... 10
flyttal, float = 1.2     skriv alltid flyttal med punkt som decimal
boolesk, boolean = True/False    flagga eller av och på


deklarera / initiera

let value; #deklarera

"""
#initiera  (namn på variabel samt datatyp)
name = " "     #string
value = 1.3    #float
value2 = 8     #integer
check = False  #boolean

print("Hello world")
Name = input("Name: ")
Age = input("Age: ")
print("welcome", Name + " you are" + " "+ Age + " years old")
print("Age:", Age)
age_in_weeks = (int(Age) * int(54))
print("Age in weeks:", age_in_weeks)

weight = int(input("weight in KG: "))
lbs = (int(weight) * float(2.20462262185))
print("pound:", lbs)
length_in_meter = input("lengt in meter:" )
print("weight after the length in kg:",weight / (float(length_in_meter) * float(length_in_meter)) )

print("Calculator:")

x = int(input("x: "))   

y = int(input("y: "))

print(x/y, x//y)
print("svar:", x * y) 




"""
sum = x + y
sum = x - y
sum = x * y
sum = x / y
"""

print(sum)

