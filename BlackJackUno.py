import BlackJackDos
import random

file = open("pakli.txt", "r", encoding="utf8")

pakli = []

for sor in file:
    pakli.append(BlackJackDos.Jackie(sor.split("\t")))

#print("Osszes kartyak",len(pakli))
#for i in range(len(pakli)):
    #print(pakli[i].Value, pakli[i].Color, pakli[i].Name)

sajat = 0
dealer = 0

print("Az on kartyai:")
for i in range(2):
    vlami = random.randint(0, len(pakli) - 1)
    print(pakli[vlami].Value, pakli[vlami].Color, pakli[vlami].Name)
    sajat += pakli[vlami].Value
    pakli.pop(vlami)

print("Az on kartyainak erteke:",sajat)

print("A dealer kartyai:")
for i in range(2):
    masik = random.randint(0, len(pakli) - 1)
    print(pakli[masik].Value, pakli[masik].Color, pakli[masik].Name)
    dealer += pakli[masik].Value
    pakli.pop(masik)

print("A dealer kartyainak erteke:",dealer)