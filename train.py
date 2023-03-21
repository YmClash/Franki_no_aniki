import random
import secrets

class Car:
    def __int__(self,mark,annee):
        self.mark = mark
        self.annee = annee




def genere(start, ende, rang):
    random.seed(0)
    num = [random.randint(start, ende) for i in range(rang)]
    for e in num():
        if num[0] == 1:
            num
        if num[1]== 2 :
            print("Mercedes")
        if num[2] == 3 :
            print("AUDI")


    print(num)


   # print([secrets.randbelow(ende) for i in range(rang)])


allo = genere(0,3, 5)

print()

