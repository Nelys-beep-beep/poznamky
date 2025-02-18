#proměnná
text="ahoj"
cislo =1
desetine = 1.5

#načítání od uživatele
nacteniTextu = input("vypsání zprávy")
nacteniCisla =int(input("zadejte cislo"))

#vypsání do konzole
print("text")
print(cislo)
print("text",cislo)

#podminky
if(cislo==10):
    print("číslo je 10")
elif(cislo==15):
    print("číslo je 15")
else:
    print("číslo je jiné")

#cykly
for i in range(10):
    print(i)
for i in range(2,10):
    print(i)
for i in range(0,101,2):
    print(i)
for i in range(100,0,-2):
    print(i)