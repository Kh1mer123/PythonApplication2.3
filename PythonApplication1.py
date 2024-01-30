#print("***NUMBER MÄNGU ***")
#print()
##'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#while 1:
#    try:
#        a=abs(int(input("Sisestage täisarv => ")))
#        break
#    except ValueError:
#         print("See ei ole täisarv")
#         break
##'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#if a==0:
#    print("Nulliga pole mõtet midagi teha")
#else:
##'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#    print("Määrake, kui palju on paaris ja mitu paaritu numbrit")
#    print()
#    c=b=a
#    paaris=0
#    paaritu=0
#    while b>0:
#        if b%2==0:
#            paaris+=1
#        else:
#            paaritu+=1
#        b=b//10
   
#    print("Isegi numbrid:", paaris)
#    print("Kummalised numbrid:", paaritu)
#    print()
##''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#    print("*Pöörake* sisestatud number ümber")
#    print()
#    b=0
#    while a>0:
#        number=a%10
#        a=a//10
#        b=b*10
#        b+=number
#    print("*Pööratud* number", b)
#    print()
##''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#    print("Syracuse hüpoteesi testimine")
#    print()
#    if c%2==0:
#        print("s on paarisarv. Jagage 2 -ga.")
#    else:
#        print("s on paaritu arv. Korrutage 3 -ga, lisage 1 ja jagage 2 -ga.")
#    while c>1:
#        if c%2:
#            c=3*c+1
#        c//=2
#        print(c)
#    print()
#    print("Hüpotees on õige")


    1 variant

n = int(input("jõulupuude arv 1 kuni 9"))  

for i in range(n):
    print("    /V\    ", end="")
print()

for i in range(n):
    print("   / V \   ", end="")
print()

for i in range(n):  
    print("  / V V \  ", end="")
print()

for i in range(n):
    print(" /VV V VV\ ", end="")


import random
N = random.randint(1, 20)                             #Juhusliku arvu arvu genereerimine
numbers = []
for _ in range(N):
    numbers.append(random.randint(-100, 100))         #Loendi täitmine juhuslike numbritega
    positive_count = 0
for num in numbers:
    if num > 0:
        positive_count += 1                           #Positiivsete arvude loendamine
print(f"Loodud numbrid: {N}")
print("Numbrite loend:", numbers)
print(f"Количество положительных чисел: {positive_count}")  



import random
N = random.randint(1, 10)                                 #juhuslik arv 1 kuni 10
arvs = [random.randint(-10, 10) for _ in range(N)]          #juhuslike arvude vahemik
positiivne = sum(1 for num in arvs if num > 0)
print(f"Loodud {N} numbrit: {arvs}")
print(f"Positiivsete arvude arv: {positiivne}")
