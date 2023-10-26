import math


def elsofeladat():
    szamok = 0
    while szamok < 148:
        if szamok % 2 == 0:
            szamok += 2
            print(szamok, end=(" , "))
    print(150)


def masodikfeladat():
    szamlalo = 0
    szamok = 0
    while szamok < 10:
        szam = int(input(f"Kérem add meg a(z) {szamok + 1}. számot: "))
        if szam % 3 == 0:
            szamlalo += 1
        szamok += 1
    print(f"Az osztható 3-mal számok száma: {szamlalo}")


def harmadikfeladat():
    szam = int(input("Kérem adjon meg egy számot: "))

    while szam % 10 != 0:
        szam = int(input("A(z) "+str(szam)+" nem osztható 10-zel. Kérem adjon meg egy másik számot: "))

    if szam % 10 == 0:
        print("A(z) "+str(szam)+" osztható 10-zel.")


def negyedikfeladat():
    szam = int(input("Kérem adjon meg egy számot: "))

    while(szam % 2 != 0) or (szam < 10) or (szam > 99):
        szam = int(input("A(z) " + str(szam) + " vagy nem páros, vagy nem kétjegyű. Kérem adjon "
                                               "meg egy másik számot: "))

    if (szam % 2 == 0) and (szam >= 10) and (szam <= 100):
        print("A(z) " + str(szam) + " kétjegyű és páros szám.")


def otodik():
    szam = int(input("Kérem adjon meg egy számot: "))

    while(szam % 2 == 0) or (szam <= 0):
        szam = int(input("A(z) " + str(szam) + " vagy nem páratlan, vagy nem pozitív."
                                               " Kérem adjon meg egy másik számot: "))

    if (szam % 2 == 1) and (szam > 0):
        print("A(z) " + str(szam) + " pozitív és páratlan szám.")


def hatodik():
    szam = int(input("Kérem adjon meg egy számot: "))

    while not ((szam % 3 == 0) or (math.sqrt(szam) == int(math.sqrt(szam)))):
        szam = int(input("A(z) " + str(szam) + " vagy nem osztható 3-mal, vagy nem négyzetszám."
                                               " Kérem adjon meg egy másik számot: "))

    print("A(z) " + str(szam) + " vagy osztható 3-mal vagy négyzetszám.")


def hetedik():
    a = float(input("Kérem adjon meg egy számot: "))
    b = float(input("Kérem adjon meg egy számot: "))
    c = float(input("Kérem adjon meg egy számot: "))
    while not ((a + b > c) and (a + c > b) and (b + c > a)):
        print("Ez a háromszög nem szerkeszthető")
        a = float(input("Kérem adjon meg egy számot: "))
        b = float(input("Kérem adjon meg egy számot: "))
        c = float(input("Kérem adjon meg egy számot: "))

    print("Ez egy szerkeszthető háromszög!")


def nyolcadik():
    maxbetu = input("Kérem írjon ide valamit, ami minimum 3 karakterből áll: ")
    while not len(maxbetu) >= 3:
        maxbetu = input("Kérem írjon ide valamit, ami minimum 3 karakterből áll: ")
    print(maxbetu.upper())


def kilencedik():
    maxbetu = input("Kérem írjon ide valamit: ")
    while not (len(maxbetu) >= 4 and (maxbetu.islower())):
        maxbetu = input("Kérem írjon ide valamit: ")
    print(maxbetu)
