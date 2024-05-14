import random
import time


def test_pary_macierz():
    #  1 2 3
    #  4 5 6
    #  7 8 9
    wynik = [[1, 4], [4, 1], [2, 5], [5, 2], [3, 6], [6, 3], [4, 7], [7, 4], [5, 8], [8, 5], [6, 9], [9, 6]]
    macierz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    pary=pary_z_macierzy(macierz)
    assert wynik == pary


def test_pary_slownik():
    #  1 2 3
    #  4 5 6
    #  7 8 9
    wynik = [[1, 4], [4, 1], [2, 5], [5, 2], [3, 6], [6, 3], [4, 7], [7, 4], [5, 8], [8, 5], [6, 9], [9, 6]]
    slownik={1: [1, 2, 3],
           2: [4, 5, 6],
           3: [7, 8, 9]}
    pary=pary_z_slownika(slownik)
    assert wynik == pary


def test_walka():
    a=["piechurzy",0]
    b=["konnica",0]
    c=["artylerzysci",0]
    assert walka(a,b)==0.5
    assert walka(b,a)==2.0
    assert walka(a,c)==0.5
    assert walka(c,a)==2.0
    assert walka(b,c)==1.5
    assert walka(c,b)==0.5

def losowanie_slownika():
    slownik_losowany={1:0,
                      2:0,
                      3:0}
    losowa_lista=[]
    losowa_lista=random.sample(range(1,10),9)
    slownik_losowany[1]=losowa_lista[:3]
    slownik_losowany[2]=losowa_lista[3:6]
    slownik_losowany[3]=losowa_lista[6:]
    print(slownik_losowany)
    return slownik_losowany

def pary_z_macierzy(macierz):
    pary=[]
    for l in range(2):
        for k in range(3):
            a=macierz[l]
            b=macierz[l+1]
            pary.append([a[k],b[k]])
            pary.append([b[k],a[k]])
    return pary

def pary_z_slownika(slownik):
    pary=[]
    for i in range(1,3):
        for j in range(3):
            c=slownik[i]
            d=slownik[i+1]
            pary.append([c[j],d[j]])
            pary.append([d[j],c[j]])
    return pary

def losowanie_armii(x):
    armia=[]
    for i in range(3):
        y=random.randint(1,x//2)
        z=random.randint(1,3)
        typ=""
        if z==1:
            typ="konnica"
            x=x-y*2
            armia.append([typ,y])
        elif z==2:
            typ="piechurzy"
            x=x-y
            armia.append([typ,y])
        else:
            typ="artylerzysci"
            while y*3>x:
                y=y-1
            x = x-y*3
            armia.append([typ, y])
    return armia

def walka(a,b):
    mnoznik=1.0
    if a[0]=="piechurzy":
        if b[0]=="piechurzy":
            mnoznik=1.0
        elif b[0]=="konnica":
            mnoznik=0.5
        else:
            mnoznik=0.5
    elif a[0]=="konnica":
        if b[0]=="piechurzy":
            mnoznik=2.0
        elif b[0]=="konnica":
            mnoznik=1
        else:
            mnoznik=1.5
    else:
        if b[0]=="piechurzy":
            mnoznik=2.0
        elif b[0]=="konnica":
            mnoznik=0.5
        else:
            mnoznik=1.0
    return mnoznik

def gra_w_fasolki(x):
    slownik_szukany=losowanie_slownika()

    while x!=0:
        odpowiedz = [[], [], []]
        pary_znalezione=0
        a = 1
        wynik=1

        print("Podaj swoje imie/swoj nick:")
        imie=input()

        for j in range(3):
            k=1
            while k==1:
                u=1
                print("Podaj ",j+1," rzad:")
                tup=input().split()
                if len(tup) != 3:
                    print("Rzad powinien miec 3 liczby!")
                    k = 1
                    continue
                try:
                    for i in tup:
                        i=int(i)
                        if i<1 or i>9:
                            print("Podales liczbe mniejsza od 1 lub wieksza od 9!")
                            u=0
                        odpowiedz[j].append(i)
                    if u==1:
                        k+=1
                except ValueError:
                    print("Podales inny typ danych niz liczba")

            del tup

        if odpowiedz==list(slownik_szukany.values()):
            print("Brawo! Znalazles prawidlowa kombinacje!")
            #wynik_eksport_przed=[]
            #wynik_eksport_po=[]
            #linie=''
            #with open('wyniki.txt') as f:
             #   for line in f:
              #      linie=linie+line.strip()
            #for i in linie:
             #   if int(i[1])<wynik:
              #      wynik_eksport_przed.append(i)
               # else:
                #    wynik_eksport_po.append(i)
            #print(wynik_eksport_przed)
            #print(wynik_eksport_po)
            wyniki=open('wyniki.txt','a+')
            lista=[imie,wynik]
            #wyniki.writelines(wynik_eksport_przed)
            wyniki.write('\n')
            wyniki.writelines(str(lista))
            wyniki.write(',')
            #wyniki.writelines(wynik_eksport_po)
            wyniki.close()

            return 0

        pary_szukane=pary_z_slownika(slownik_szukany)
        pary_podane=pary_z_macierzy(odpowiedz)
        for m in pary_podane:
            if m in pary_szukane:
                pary_znalezione+=1

        pasujace_liczby=0
        lista_slownik = list(slownik_szukany.values())
        for i in range(3):
            lista_wyniki=lista_slownik[i]
            odpowiedz_wyniki=odpowiedz[i]
            for j in range(3):
                if lista_wyniki[j]==odpowiedz_wyniki[j]:
                    pasujace_liczby+=1

        print(pary_szukane)
        print(pary_podane)

        print("ile par liczb w pionie jest zgodnych:", pary_znalezione)
        print("ile liczb zgadza sie:", pasujace_liczby)

        while a!=0:
            x=1
            print("Czy chcesz kontynuwac?[0-Nie, Inne liczby-Tak]")
            x=input()
            a=0
            try:
                x=int(x)
            except ValueError:
                print("Podales inny typ danych niz liczba")
                a=1

        wynik+=1

    return 0


def bitwa():
    budzet=1000
    zwiady=0
    imie="x"
    armia_przeciwnika=0
    armia=[]
    trudnosc=''
    t=0
    odpowiedz=0
    ktore=2
    liczebnosc=0
    typ_jednostki="piechurzy"

    while t==0:
        print("Jaki poziom trudnosci wybierasz?")
        print("1: łatwy - armia do pokonania za 600punktow")
        print("2: średni - armia do pokonania za 800punktów")
        print("3: trudny - armia do pokonania za 1000punktów")
        trudnosc=input()
        try:
            trudnosc=int(trudnosc)
            if trudnosc==1:
                armia_przeciwnika=losowanie_armii(600)
                t=1
            elif trudnosc==2:
                armia_przeciwnika=losowanie_armii(800)
                t=1
            elif trudnosc==3:
                armia_przeciwnika=losowanie_armii(1000)
                t=1
            else:
                print("Nie ma podanego poziomu trudnosci")
        except ValueError:
            print("Podałeś inny tryb danych niź liczba")

    while x!=0:
        print("Podaj swoje imie/nick")
        imie=input()
        print("Masz do dyspozycji:",budzet,"złotych monet")
        print("Możesz wydać 100 monet aby wysłać zwiad i dowiedzieć się jak wygląda jedno ze skrzydeł wroga (lub wiecej skrzydel 100monet = 1zwiad)")
        print("Czy chcesz to zrobić? (od 1 do 3) - Tak, podaj ile skrzydeł chcesz sprawdzić, 0 - Nie")
        odpowiedz=input()
        try:
            odpowiedz=int(odpowiedz)
            if odpowiedz<0 or odpowiedz>3:
                print("Nie ma takiej ilosci skrzydel")
            else:
                for i in range(odpowiedz):
                    v=1
                    zwiady += 1
                    while v==1:
                        print("Ktore skrzydlo chcesz sprawdzic?")
                        print("1 - lewe, 2 - środek, 3 - prawe")
                        ktore=input()
                        try:
                            ktore=int(ktore)
                            if ktore==1:
                                print(armia_przeciwnika[0])
                                budzet=budzet-100
                                v=0
                            elif ktore==2:
                                print(armia_przeciwnika[1])
                                budzet = budzet - 100
                                v = 0
                            elif ktore==3:
                                print(armia_przeciwnika[2])
                                budzet = budzet - 100
                                v = 0
                            else:
                                print("Podana liczba nie reprezentuje zadnego skrzydla!")
                        except ValueError:
                            print("Podales inny typ danych niz liczba")

        except ValueError:
            print("Podales inny typ danych niz liczba")
            continue

        for j in range(3):
            v=1
            while v == 1:
                print("Masz do dyspozycji:", budzet, "złotych monet")
                if j==0:
                    print("Wybierz jaka jednostke chcesz na lewym skrzydle i jaka ona bedzie miala liczebnosc:")
                elif j==1:
                    print("Wybierz jaka jednostke chcesz na środku i jaka ona bedzie miala liczebnosc:")
                else:
                    print("Wybierz jaka jednostke chcesz na prawym skrzydle i jaka ona bedzie miala liczebnosc:")
                print("Podaj typ jednostki: piechurzy/konnica/artylerzysci")
                typ_jednostki=input()
                print("Podaj jej liczebnosc:")
                liczebnosc=input()

                try:
                    liczebnosc=int(liczebnosc)
                    if typ_jednostki.lower() == "piechurzy":
                        if liczebnosc >= 0:
                            if liczebnosc > budzet:
                                print("Przekroczyles swoj budzet")
                            else:
                                armia.append([typ_jednostki.lower(), liczebnosc])
                                budzet=budzet-liczebnosc
                                v = 0
                        else:
                            print("Podana liczebnosc nie moze byc ujemna!")
                    elif typ_jednostki.lower() == "artylerzysci":
                        if liczebnosc >= 0:
                            if liczebnosc * 2 > budzet:
                                print("Przekroczyles swoj budzet")
                            else:
                                armia.append([typ_jednostki.lower(), liczebnosc])
                                budzet = budzet - liczebnosc*2
                                v = 0
                        else:
                            print("Podana liczebnosc nie moze byc ujemna!")
                    elif typ_jednostki.lower() == "konnica":
                        if liczebnosc >= 0:
                            if liczebnosc * 3 > budzet:
                                print("Przekroczyles swoj budzet")
                            else:
                                armia.append([typ_jednostki.lower(), liczebnosc])
                                budzet = budzet - liczebnosc*3
                                v = 0
                        else:
                            print("Podana liczebnosc nie moze byc ujemna!")
                    else:
                        print("Zle podales typ jednostki!")
                except ValueError:
                    print("Podana liczebnosc nie jest liczba!")

        print("Bitwa!")
        time.sleep(1)
        print("Walka na lewym skrzydle")
        print("Twoj oddzial:")
        print(armia[0])
        print("Oddzial wroga:")
        print(armia_przeciwnika[0])
        time.sleep(3)
        print(".", end="")
        time.sleep(2)
        b = armia_przeciwnika[0]
        a = armia[0]
        nasz_wspolczynnik = walka(a, b)
        print(".",end="")
        szczescie=random.randint(50,150)
        szczescie=szczescie*0.01
        time.sleep(2)
        print(".")
        time.sleep(2)
        if a[1]*nasz_wspolczynnik*szczescie>b[1]:
            print("Brawo! Wygrales walke na lewym skrzydle!")
            print("Z twojego oddzialu pozostalo:")
            a[1]=(a[1]*nasz_wspolczynnik*szczescie)//1-b[1]
            b[1] = 0
            print(a)
        else:
            print("Przegrales na lewym skrzydle!")
            print("Przeciwnikowi na lewym skrzydle pozostalo:")
            b[1]=b[1]-(a[1]*nasz_wspolczynnik*szczescie)//1
            a[1]=0
            print(b)
        time.sleep(3)

        print("Walka na prawym skrzydle")
        print("Twoj oddzial:")
        print(armia[2])
        print("Oddzial wroga:")
        print(armia_przeciwnika[2])
        time.sleep(3)
        print(".", end="")
        time.sleep(2)
        b = armia_przeciwnika[2]
        a = armia[2]
        nasz_wspolczynnik = walka(a, b)
        print(".", end="")
        time.sleep(2)
        szczescie = random.randint(50, 150)
        szczescie = szczescie * 0.01
        print(".")
        time.sleep(2)
        if a[1] * nasz_wspolczynnik * szczescie > b[1]:
            print("Brawo! Wygrales walke na prawym skrzydle!")
            print("Z twojego oddzialu pozostalo:")
            a[1] = (a[1] * nasz_wspolczynnik * szczescie)//1 - b[1]
            b[1] = 0
            print(a)
        else:
            print("Przegrales na prawym skrzydle!")
            print("Przeciwnikowi na prawym skrzydle pozostalo:")
            b[1] = b[1] - (a[1] * nasz_wspolczynnik * szczescie)//1
            a[1] = 0
            print(b)

        time.sleep(5)
        print("Finał!")
        print("Walka w centrum")
        print("Nasze sily")
        print(armia)
        print("Sily przeciwnika")
        print(armia_przeciwnika)
        time.sleep(3)
        print(".", end="")
        time.sleep(3)
        print(".", end="")
        time.sleep(3)
        print(".", end="")
        time.sleep(3)

        a=armia_przeciwnika[0]
        b=armia_przeciwnika[1]
        c=armia_przeciwnika[2]
        ich_wartosc_bojowa=b[1]+walka(a,b)*a[1]+walka(c,b)*c[1]
        d=armia[0]
        e=armia[1]
        f=armia[2]
        nasza_wartosc_bojowa=e[1]+walka(d,e)*d[1]+walka(f,e)*f[1]
        nasz_wspolczynnik=walka(e,b)
        szczescie = random.randint(50, 150)
        szczescie = szczescie * 0.01
        if nasz_wspolczynnik*nasza_wartosc_bojowa*szczescie>ich_wartosc_bojowa:
            print("Brawo! Wygrales cala bitwe!")
            nasza_wartosc_bojowa=nasz_wspolczynnik*nasza_wartosc_bojowa*szczescie-ich_wartosc_bojowa
            nasza_wartosc_bojowa=nasza_wartosc_bojowa//1
            print("Pozostala wartosc bojowa twojej armii to:")
            print(e[0],nasza_wartosc_bojowa)
            print("Twoj wynik zostanie zapisany w tabeli wynikow")

            wyniki = open('wyniki2.txt', 'a+')
            score=walka(e,["piechurzy",0])*nasza_wartosc_bojowa
            wyniki.write('\n')
            wyniki.write(imie+": "+str(score)+" zwiady:"+str(zwiady))
            wyniki.write(',')
            wyniki.close()
            return 0
        else:
            print("Przegrales cala bitwe!")
            ich_wartosc_bojowa=ich_wartosc_bojowa-nasz_wspolczynnik*nasza_wartosc_bojowa*szczescie
            ich_wartosc_bojowa=ich_wartosc_bojowa//1
            print("Pozostala wartosc bojowa armii przeciwnika to:")
            print(b[0],ich_wartosc_bojowa)
            return 0

t=1
while t==1:
    print("W jaka gre chcesz zagrac?")
    print("2 - bitwa")
    print("1 - gra w fasolki")
    print("0 - zakoncz program")
    x=input()
    try:
        x=int(x)
        if x == 1:
            gra_w_fasolki(1)
        elif x == 2:
            bitwa()
        elif x==0:
            t=0
        else:
            print("Nie ma dostepnej gry pod podanym numerem")
    except ValueError:
        print("Podales inny typ danych niz liczba")