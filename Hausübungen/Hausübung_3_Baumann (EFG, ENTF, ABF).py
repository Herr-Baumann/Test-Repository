# Erweitern Sie das Wörterbuch - Beispiel
# um die Möglichkeit, Einträge zu ergänzen bzw.
# zu löschen

wörterbuch_deutsch = ["Apfel", "Birne", "Kirsche", "Melone", "Marille", "Pfirsich"]
wörterbuch_englisch = ["apple", "pear", "cherry", "melon", "apricot", "peach"]
max = len(wörterbuch_deutsch)

running = True
while running:
    auswahl = input( "Befehl? [E]infügen, [L]öschen, [A]bfragen:")
        
    if auswahl == 'E' or auswahl =='e':
        x = wörterbuch_deutsch.append(input("Was möchten Sie einfügen?"))
        print(wörterbuch_deutsch)
    elif auswahl == 'L' or auswahl =='l':
        y = wörterbuch_deutsch.remove(input("Was möchten Sie löschen?"))
        print(wörterbuch_deutsch)
    elif auswahl == 'A' or auswahl =='a':
        running = False



eingabe = input("Deutscher Begriff:")
index = 0

while index < max:
    if wörterbuch_deutsch[index].lower() == eingabe.lower():
        print(wörterbuch_englisch[index])
        break
    index +=1

if index == max:
    print("nicht gefunden")

    