"""
Marius Fiksdal
marius@fiksdal.io
14.02.2021
"""

from enkelt_kortspill_fullstendig import Kortstokk, Kort


class Spill:
    def __init__(self):
        # self.kortene = Kort("type", 5)
        self.kortstokk = Kortstokk()
        self.kortstokk.stokk()
        self.plasser = list()
        for i in range(9):
            self.plasser.append([self.kortstokk.trekk()])

    def skriv_tilstand(self):
        """Skriver ut de fremste kortene og antall kort i kortstokken"""
        print("˅------KORT------˅")
        j = 0
        for i in self.plasser:
            print(f"{j}: {i[-1]}")
            j += 1
        print("˄------KORT------˄")
        print(f"Antall kort: {len(self.kortstokk)}")
        # return f"Kort som ligger: {}Antall kort: {len(self.kortstokk)}"

    def er_ferdig(self):
        """Sjekker om kortstokken er 'tom'"""
        if len(self.kortstokk) < 2:
            return True
        else:
            return False

    def plasser_to_kort(self, kort_1, kort_2):
        """Sjekker om totalen er 11 og legger to kort hvis dette er sant"""
        to_kort_total = self.plasser[int(kort_1)][-1].verdi + self.plasser[int(kort_2)][-1].verdi
        if to_kort_total == 11:
            self.plasser[int(kort_1)].append(self.kortstokk.trekk())
            self.plasser[int(kort_2)].append(self.kortstokk.trekk())
            print("Summen er 11")
        else:
            print(f"Summen er ikke 11, den er:{to_kort_total}")

    def plasser_tre_kort(self, kort_1, kort_2, kort_3):
        """Sjekker om disse 3 kortene er bildekort, og legger 3 kort hvis dette er sant"""
        if any(ele in str(self.plasser[int(kort_1)][-1]) for ele in ["Konge", "Knekt", "Dame"]) and any(
                ele in str(self.plasser[int(kort_2)][-1]) for ele in ["Konge", "Knekt", "Dame"]) and any(
                ele in str(self.plasser[int(kort_3)][-1]) for ele in ["Konge", "Knekt", "Dame"]):
            print("Er bildekort!")
            self.plasser[int(kort_1)].append(self.kortstokk.trekk())
            self.plasser[int(kort_2)].append(self.kortstokk.trekk())
            self.plasser[int(kort_3)].append(self.kortstokk.trekk())
        else:
            print("Er ikke bildekort!")


if __name__ == "__main__":
    """Kodeblokk som er beskrevet i oppgaveteksten"""
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



