#2.	MegelőzőKövetkezőSzám: A program kérjen be a konzolról egy egész számot! Ha a szám egyjegyű, akkor a program írja ki a konzolra a számot megelőző és követő egész számot, egyébként ne írjon ki semmit!

szam = int(input("Adj meg egy egész számot!"))
if (szam <10) and (szam >-10):
    megelozo = int(szam-1)
    kovetkezo = int(szam+1)
    print("A(z) "+str(szam)+" szám megelőző értéke "+str(megelozo)+", következő szám értéke "+str(kovetkezo))