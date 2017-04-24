def netto_pracownik2014(kwota):
    brutto = round(float(kwota), 2)
    emeryt = (brutto * 0.0976)
    emeryt = round(float(emeryt), 2)
    renta = (brutto * 0.015)
    renta = round(float(renta), 2)
    choroba = (brutto * 0.0245)
    choroba = round(float(choroba), 2)
    suma_posr = emeryt + renta + choroba
    suma_posr = round(suma_posr, 2)
    netto_posr = brutto - suma_posr
    zdrow = (netto_posr * 0.09)
    zdrow = round(float(zdrow), 2)
    zdrow2 = (netto_posr * 0.0775)
    zdrow2 = round(float(zdrow2), 2)
    podstawa_podatki = netto_posr - 111.25
    podstawa_podatki = round(podstawa_podatki, 0)
    podatki = (podstawa_podatki * 0.18)
    podatki = (podatki - 46.33)
    podatki = (podatki - zdrow2)
    podatki = round(float(podatki), 0)
    netto_end = netto_posr - zdrow - podatki
    netto_end = round(float(netto_end), 2)
    return '%.2f' % netto_end


def skladki_pracodawca(kwota):
    brutto = round(float(kwota), 2)
    emeryt = round((brutto * 0.0976), 2)
    renta = round((brutto * 0.065), 2)
    wypadek = round((brutto * 0.0193), 2)
    fundusz_pow = round((brutto * 0.0245), 2)
    fundusz_gsp = round((brutto * 0.001), 2)
    koszt_pracodawca = emeryt + renta + wypadek + fundusz_pow + fundusz_gsp
    koszt_pracodawca = round(float(koszt_pracodawca), 2)
    return koszt_pracodawca


def sum_pracodawca(kwota):
    brutto = round(float(kwota), 2)
    lacznie = brutto + skladki_pracodawca(brutto)
    lacznie = round(float(lacznie), 2)
    return lacznie

wejscie = input()
liczba_prac = int(wejscie)
liczba_prac2 = int(wejscie)
suma_pracodawca_wszyscy = 0.00
pracownicy = []
wyniki = []

if liczba_prac == 1:
    pracownik = input()
    pracownik_kwota = input()
    print(pracownik, '%.2f' % float(netto_pracownik2014(pracownik_kwota)), '%.2f' % float(skladki_pracodawca(pracownik_kwota)), '%.2f' % float(sum_pracodawca(pracownik_kwota)))
    suma_pracodawca_wszyscy = sum_pracodawca(pracownik_kwota)
    print(suma_pracodawca_wszyscy)
else:
    while liczba_prac != 0:
        wejscie = input()
        pracownicy = wejscie.split()
        pracownicy.append(pracownicy[0])
        pracownik = str(pracownicy[0]),str(netto_pracownik2014(pracownicy[1])),str(skladki_pracodawca(pracownicy[1])),str(sum_pracodawca(pracownicy[1]))
        wyniki.append(pracownik)
        suma_pracodawca_wszyscy = suma_pracodawca_wszyscy + sum_pracodawca(pracownicy[1])
        del pracownicy[:]
        liczba_prac -= 1
    for i in range(0, len(wyniki)):
        print(wyniki[i])
    print(round(float(suma_pracodawca_wszyscy), 2))
	print("Ta wersja jest juz ostateczna i dziala!")
	print("Lubie placki")