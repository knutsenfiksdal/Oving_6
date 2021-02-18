from enkelt_kortspill_fullstendig import Kortstokk, Kort



k1 = Kort


class Spill:
    def __init__(self):
        # self.kortene = Kort("type", 5)
        self.kortstokk = Kortstokk()
        self.kortstokk.stokk()
        self.plasser = list()
        for i in range(9):
            self.plasser.append([self.kortstokk.trekk()])

    def skriv_tilstand(self):
        print("˅------KORT------˅")
        for i in self.plasser:
            print(i[-1])
        print("˄------KORT------˄")

        print(f"Antall kort: {len(self.kortstokk)}")
        # return f"Kort som ligger: {}Antall kort: {len(self.kortstokk)}"

    def er_ferdig(self):
        if len(self.kortstokk) == 0:
            return True
        else:
            return False

    def plasser_to_kort(self, kort_1, kort_2):
        to_kort_total = self.plasser[int(kort_1)][0].verdi + self.plasser[int(kort_2)][0].verdi
        if to_kort_total == 11:
            self.plasser[int(kort_1)].append(self.kortstokk.trekk())
            self.plasser[int(kort_2)].append(self.kortstokk.trekk())
            print("Summen er 11")
        else:
            print("Summen er ikke 11")

    def plasser_tre_kort(self, kort_1, kort_2, kort_3):
        if any(ele in str(self.plasser[int(kort_1)][0]) for ele in ["Konge", "Knekt", "Dame"]) and any(
                ele in str(self.plasser[int(kort_2)][0]) for ele in ["Konge", "Knekt", "Dame"]) and any(
            ele in str(self.plasser[int(kort_3)][0]) for ele in ["Konge", "Knekt", "Dame"]):

            print("Er bildekort!")
            self.plasser[int(kort_1)].append(self.kortstokk.trekk())
            self.plasser[int(kort_2)].append(self.kortstokk.trekk())
            self.plasser[int(kort_3)].append(self.kortstokk.trekk())
        else:
            print("Er ikke bildekort!")


if __name__ == "__main__":
    spel = Spill()
    while not spel.er_ferdig():
        spel.skriv_tilstand()
        print("Skriv inn 2 eller 3 indekser(1 2 3)")

        usr_input = input("--> ")
        usr_input = list(map(int, usr_input.strip().split()))
        if len(usr_input) == 3:
            spel.plasser_tre_kort(usr_input[0], usr_input[1], usr_input[2])
        elif len(usr_input) == 2:
            spel.plasser_to_kort(usr_input[0], usr_input[1])
        else:
            print("Skriv inn 2 elle 3 din tosk")
    print("---FERDIG---")

spel = Spill()
spel.skriv_tilstand()
print()

print(spel.kortstokk.neste_kort().verdi)

spel.plasser_to_kort(2, 3)

spel.plasser_tre_kort(0, 1, 2)

"""
        if self.kortstokk.neste_kort().verdi < to_kort_total:
            pass
            
            
str(self.plasser[int(kort_1)][0]) in ["Konge", "Knekt", "Dame"]:


        spel.plasser_to_kort(input("Skriv inn første indeks: "), input("Skriv inn andre indeks: "))


"""
