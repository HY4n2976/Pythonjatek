import random
class FeketeJani:
    def __init__(self, pakli):
        self.Value = int(pakli[0])
        self.Color = pakli[1]
        self.Name = pakli[2].strip("\n")

    def Kartyak(self):
        print("Az on kartyai:", )