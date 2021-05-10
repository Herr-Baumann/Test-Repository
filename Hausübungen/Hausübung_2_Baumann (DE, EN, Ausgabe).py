wörterbuch_deutsch = ["Apfel", "Birne", "Kirsche", "Melone", "Marille", "Pfirsich"]
wörterbuch_englisch = ["apple", "pear", "cherry", "melon", "apricot", "peach"]

max = len(wörterbuch_deutsch)
eingabe = input("Eingabe, zu übersetzender Bergriff:")
index = 0


while index < max:
    if wörterbuch_deutsch[index].lower() == eingabe.lower():
        print(wörterbuch_englisch[index], "EN")
        break
    elif wörterbuch_englisch[index].lower() == eingabe.lower():
        print(wörterbuch_deutsch[index], "DE")
        break
    index +=1
if index == max:
    print("nicht gefunden")



    

    