wörterbuch_deutsch = {"Apfel": "apple",
                      "Birne": "pear",
                      "Kirsche" : "cherry",
                      "Melone": "melon",
                      "Marille": "apricot",
                      "Pfirsich": "peach"}
wörterbuch_englisch = {"apple": "Apfel",
                      "pear": "Birne",
                      "cherry": "Kirsche",
                      "apricot": "Marille",
                      "peach": "Pfirsich"}
running = True
while running:
    try:
        auswahl = input("""Für die Übersetzung DE -> EN geben Sie 'D' oder 'd' ein.
Für die Übersetzung EN -> DE geben Sie 'E' oder 'e' ein.
Um das Programm zu beenden geben Sie 'B' oder 'b' ein.
\033[1mIhre Auswahl:\033[0m""")
            
        if auswahl == 'D' or auswahl =='d':
            eingabe = input("Geben Sie ein deutsches Wort zum übersetzen ein:")
            eingabe = eingabe.capitalize()
            print("\033[1m Ihre Übersetzung ist: \033[0m", wörterbuch_deutsch[eingabe])
        elif auswahl == 'E' or auswahl =='e':
            eingabe_1 = input("Geben Sie ein englisches Wort zum übersetzen ein:")
            eingabe_1 = eingabe_1.lower()
            print("\033[1m Ihre Übersetzung ist: \033[0m", wörterbuch_englisch[eingabe_1])
        elif auswahl == 'B' or auswahl == 'b':
            running = False

    except KeyError:
        print("\033[1mBegriff nicht gefunden. Bitte um Neueingabe:\033[0m")

