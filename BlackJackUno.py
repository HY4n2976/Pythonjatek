import BlackJackDos
import random

file = open("pakli.txt", "r", encoding="utf8")

pakli = []

for sor in file:
    pakli.append(BlackJackDos.Jackie(sor.split("\t")))

#print("Osszes kartyak",len(pakli))
#for i in range(len(pakli)):
    #print(pakli[i].Value, pakli[i].Color, pakli[i].Name)

penz = int(input("Mennyit kivan kockaztatni?"))

while penz < 0 or penz == 0:
    print("Nuh uh! Minuszban nem jatszhatsz!")
    penz = int(input("Szzooovaal mennyit kivan kockaztatni?"))

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

milegyen = int(input("Mit szeretnel tenni?, Ha kersz lapot: 0, ha double down: 1, ha bedobod: 2"))

while milegyen < 0 or milegyen > 2:
    print("Megint hulye vagy ember!")
    milegyen = int(input("Mit akarsz csinalni?!, Ha kersz lapot: 0, ha double down: 1, ha bedobod: 2"))

if milegyen == 0:
    vlami = random.randint(0, len(pakli) - 1)
    print("Az uj kartyad:", pakli[vlami].Value, pakli[vlami].Color, pakli[vlami].Name)
    sajat += pakli[vlami].Value
    pakli.pop(vlami)
    milegyen = int(input("Mit szeretnel tenni?, Ha kersz lapot: 0, ha double down: 1, ha bedobod: 2"))

    while milegyen < 0 or milegyen > 2:
        print("Megint hulye vagy ember!")
        milegyen = int(input("Mit akarsz csinalni?!, Ha kersz lapot: 0, ha double down: 1, ha bedobod: 2"))

    print("Kartyaid uj erteke:", sajat)
if milegyen == 1:
    vlami = random.randint(0, len(pakli) - 1)
    print("Az uj kartyad:", pakli[vlami].Value, pakli[vlami].Color, pakli[vlami].Name)
    sajat += pakli[vlami].Value
    pakli.pop(vlami)
    print("Kartyaid uj erteke:", sajat)

if milegyen == 2:
    print("Jatek vege. Sajna vesztettel, de ha nem dobtad volna be akkor lehet nyertel volna :/")

