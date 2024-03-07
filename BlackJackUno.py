import BlackJackDos
import random

file = open("pakli.txt", "r", encoding="utf8")

pakli = []

for sor in file:
    pakli.append(BlackJackDos.FeketeJani(sor.split("\t")))

print("Osszes kartyak",len(pakli))
for i in range(len(pakli)):
    print(pakli[i].Value, pakli[i].Color, pakli[i].Name)