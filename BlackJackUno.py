import BlackJackDos
import random

file = open("pakli.txt", "r", encoding="utf8")

pakli = []

for sor in file:
    pakli.append(BlackJackDos.Jackie(sor.split("\t")))

#print("Osszes kartyak",len(pakli))
#for i in range(len(pakli)):
    #print(pakli[i].Value, pakli[i].Color, pakli[i].Name)

print("Az on kartyai:")
for i in range(2):
    vlami = random.randint(0, len(pakli) - 1)
    print(pakli[vlami].Value, pakli[vlami].Color, pakli[vlami].Name)
    pakli.pop(vlami)

print("A dealer kartyai:")
for i in range(2):
    vlami = random.randint(0, len(pakli) - 1)
    print(pakli[vlami].Value, pakli[vlami].Color, pakli[vlami].Name)
    pakli.pop(vlami)