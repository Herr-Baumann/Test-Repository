# Aufgabe zur Annäherung an den Wert Pi über die Leibnitzreihe
y = 0
x = 1

n = int(input("Zahl:"))

for k in range(0,n):
    y += x/(2*k+1)
    y = y * (-1)

print("Annäherung an PI:", abs(y*4))


