print ("Cześć jestem twoim kalkulatorem BMI")

wiek = int(input("Wprowadź swój wiek: "))
imie = input("Jak masz na imię?: ")
waga = input("Wprowadź swoją wagę [kg]: ")
wzrost_cm = int(input("Wprowadź swój wzrost [cm]: "))
wzrost_m = float(wzrost_cm / 100)
bmi = float(waga) / (wzrost_m ** 2)
wartosc_bmi_1 = round(bmi, 2)
wartosc_bmi_2 = str(wartosc_bmi_1)

print (imie + ", twoje BMI wynosi " + wartosc_bmi_2)

ryzyko_1 = """Ryzyko chorób towarzyszących otyłości: minimalne,
ale zwiększony poziom wystąpienia innych problemów zdrowotnych"""
optymalna = """Optymalna masa ciała.
Ryzyko chorób towarzyszących otyłości: minimalne"""

if wartosc_bmi_1 <= 16:
    print ("Wygłodzenie" + ryzyko_1)
elif wartosc_bmi_1 <= 16.99:
    print ("Wychudzenie" + ryzyko_1)
elif wartosc_bmi_1 <= 18.49:
    print ("Niedowaga" + ryzyko_1)
    
elif (19 <= wartosc_bmi_1 <= 24) and (19 <= wiek <= 24):
    print (optymalna)
    
elif (20 <= wartosc_bmi_1 <= 25) and (25 <= wiek <= 34):
    print (optymalna)

elif (21 <= wartosc_bmi_1 <= 26) and (35 <= wiek <= 44):
    print (optymalna)

elif (22 <= wartosc_bmi_1 <= 27) and (45 <= wiek <= 54):
    print (optymalna)

elif (23 <= wartosc_bmi_1 <= 28) and (55 <= wiek <= 64):
    print (optymalna)

elif (24 <= wartosc_bmi_1 <= 29) and (wiek >= 64):
    print (optymalna)
    
elif wartosc_bmi_1 <= 29.99:
    print ("""Nadwaga.
Ryzyko chorób towarzyszących otyłości: średnie""")
elif wartosc_bmi_1 <= 34.99:
    print ("""Otyłość I stopnia.
Ryzyko chorób towarzyszących otyłości: wysokie""")
elif wartosc_bmi_1 <= 39.99:
    print ("""Otyłość II stopnia.
Ryzyko chorób towarzyszących otyłości: bardzo wysokie""")
elif wartosc_bmi_1 >= 40:
    print ("""Otyłość III stopnia.
Ryzyko chorób towarzyszących otyłości: ekstremalne""")
else:
    print ("BŁĄD")
