# Dies ist das erste Phyton-Programm im Zuge der LV INDIT1!
print("Hello, PTO!") # Kommentar

#Mehrzeilige Kommentare ...
# ... müssen in JEDER Zeile eine Raute am Beginn stehen haben

"""
Oder aber ich kann einen mehrzeiligen String mittels 3 Anführungszeichen
verwenden --> ACHTUNG: PyDoc!(um Softwaredokumentation zu erstellen) würde dies
als Beschreibung verwenden. (In die Dokumentation übernehmen)
Die Rauten nicht verwendet werden würden.
"""

# Programmbestandteile:
# - Anweisungen
# - Variablen / Daten -> benötigt Bezeichner(Name der Variable z.B.: Buchstabe)

# Leerzeichen können gesetzten werden wie man will (x=1 oder x = 1)

x_Koordinate = 1 # Zuweisung an Variable (fixer Wert)
print(x_Koordinate)
print("x_Koordinate:", x_Koordinate)
print(type(x_Koordinate))

text = "Ich bin ein Text" # bezeichnet man als String (Zeichenkette)
print(text)
print(type(text))
print(id(text))
text = 123
print(text)
print(type(text))
print(id(text))

reele_zahl = 123.4567

# Operatoren
# -Mathematische operatoren
# -> +,-,*,/, 2 Divisionen 1 mal (/) und doppelt (//)

# EIngabe von der Konsole (=Tastatur)
meine_Zahl = input("Eingabe einer Zahl:")
print("Die Eingabe lautete:", meine_Zahl)
