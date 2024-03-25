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

if dealer == 21:
    print("A dealer nyert sajna a penzedet elbuktad :/")
elif sajat == 21:
    print("Nyerteeell!!! A nyeremenyed osszege:", "$",penz * 2)
elif sajat > 21:
    print("vesztettel mert ket aszt kaptal en meg lusta voltam megcsinalni bocsesz ¤-¤")
else:
    milegyen = int(input("Mit szeretnel tenni?, Ha kersz lapot: 0, ha double down: 1, ha varsz: 2 "))

    while milegyen < 0 or milegyen > 2:
        print("Megint hulye vagy ember!")
        milegyen = int(input("Mit akarsz csinalni?!, Ha kersz lapot: 0, ha double down: 1, ha varsz: 2 "))

    if milegyen == 0:
        vlami = random.randint(0, len(pakli) - 1)
        print("Az uj kartyad:", pakli[vlami].Value, pakli[vlami].Color, pakli[vlami].Name)
        sajat += pakli[vlami].Value
        pakli.pop(vlami)
        print("Kartyaid uj erteke:", sajat)

    while milegyen < 0 or milegyen > 2:
        print("Kikeszitesz komolyan ˘`-´˘")
        milegyen = int(input("Mitcsinalsz?!, Ha kersz lapot: 0, ha double down: 1, ha varsz: 2 "))

    if sajat < 21 and not milegyen == 1 and not milegyen == 2:
        milegyen = int(input("Mit szeretnel tenni?, Ha kersz lapot: 0, ha double down: 1, ha varsz: 2 "))
        if milegyen == 0 and not sajat > 21:
            print("Az uj kartyad:", pakli[vlami].Value, pakli[vlami].Color, pakli[vlami].Name)
            sajat += pakli[vlami].Value
            pakli.pop(vlami)
            print("Kartyaid uj erteke:", sajat)
        elif milegyen == 0 and sajat > 21:
            print("Veszitettel legkozelebb jobb lesz!!")

    elif sajat == 21:
        print("Nyerteeell!!! A nyeremenyed osszege:", "$",penz*2 )
    elif sajat > 21:
        print("Vesztettel nem folytatodik a jatek es meg a penzed is elvesztetted hahaa bena vagy XD!!")

    while milegyen < 0 or milegyen > 2:
        print("Meg mindig nem birsz magaddal ugye? hat jo ¯\_(ツ)_/¯")
        milegyen = int(input("Deee mit szeretnel csinalni?, Ha kersz lapot: 0, ha double down: 1, ha varsz: 2 "))

    if milegyen == 1:
        vlami = random.randint(0, len(pakli) - 1)
        print("Az uj kartyad:", pakli[vlami].Value, pakli[vlami].Color, pakli[vlami].Name)
        sajat += pakli[vlami].Value
        pakli.pop(vlami)
        print("Kartyaid uj erteke:", sajat)
        print("Kockaztatott penzosszeg:", "$",penz*2)
        if sajat > 21:
            print("Hahhhaaaaa elbuktaadd azthitted majd jol megszeded magad penzzel mi? Haaatt nem XDD!!")


    if milegyen == 2 or milegyen == 1 and not sajat >= 21 or milegyen == 0 and not sajat >= 21:
        print("Na varj egy picit nem egyedul jatszasz °-°")
        if dealer <= 17:
            masik = random.randint(0, len(pakli) - 1)
            print("A dealer uj kartyaja:",pakli[masik].Value, pakli[masik].Color, pakli[masik].Name)
            dealer += pakli[masik].Value
            pakli.pop(masik)
            print("A dealer kartyainak erteke:", dealer)
            if dealer > 21 or dealer < sajat:
                print("Nyertel Ocsipook a nyeremenyed:", "$",penz*2)
            elif dealer == 21:
                print("A dealer nyert sajna a penzedet elbuktad :/")
            elif dealer < sajat and dealer < 21:
                print("Szep volt te nyerteeell! A nyeremenyed:", "$",penz*2)
            elif dealer >= 17 and dealer < 21:
                if dealer > sajat:
                    print("Nemar a Dealer nyert, a penzed is eluszott sok sikert legkozelebb :(")
                elif sajat > dealer:
                    print("Yippiee te nyerteell a nyert penzosszeg:", "$", penz * 2)
                elif sajat == dealer:
                    print("A kartyaitok erteke egyenlo, igy dontetlen lett es vissza kapod a penzed :D")
        elif dealer >= 17 and dealer < 21:
            if dealer > sajat:
                 print("Nemar a Dealer nyert, a penzed is eluszott sok sikert legkozelebb :(")
            elif sajat > dealer :
                    print("Yippiee te nyerteell a nyert penzosszeg:", "$",penz*2)
            elif sajat == dealer:
                print("A kartyaitok erteke egyenlo, igy dontetlen lett es vissza kapod a penzed :D")