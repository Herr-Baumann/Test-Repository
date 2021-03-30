# Aufgabe 1
# Schreiben SIe eine Python-Programm, dass
# 1) den Benutzer begrüßt
# 2) eine erste Zahl entgegen nimmt
# 3) eine zweite Zahl entgegen nimmt
# 4) die Summe der beiden Zahlen berechnet und ausgiebt
# 5) die Differnez der kleineren von der größeren Zahl berechnen
# 6) das Produkt der beiden Zahlen berechnet und ausgiebt
# 7) den Quotienten der kleineren Zahl durch die Größere berechnet und ausgiebt (inkl. Nachkommastellen)

# für Zahlen immer noch "int" für ganze Zahlen oder "float" für alle Reelen Zahlenvorangestellt!!!!!!!

print("Guten Tag")
print("Bei den folgen Berechnungen gibt es 2 Regeln:")
print("-> Differenz: immer größere Zahl - kleinere Zahl")
print("-> Quotient: kleinere Zahl / größere Zahl")
x=float(input("Bitte geben Sie hier eine Zahl ein:"))
y=float(input("Bitte geben Sie hier eine Zahl ein:"))

Produkt = x*y
Summe = x+y
Quotient = x/y
Quotient_gegen = y/x
Differenz = x-y
Differenz_gegen = y-x

print("Summe" , Summe)
print("Produkt" , Produkt)

if x <= y:
    print("Quotient" , Quotient)
elif x > y:
    print("Quotient" , Quotient_gegen)

if x >= y:
    print("Differenz" , Differenz)
elif x < y:
    print("Differenz" , Differenz_gegen)
# um zu sehen wo was abläuft kann man den Debuuger starten (kleine grüne Zecke ctrl F5)
# mit F6 und F7 weiterschalten

