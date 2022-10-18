from teststuff.inherit.tier import Tier

class Hund(Tier):
    """ Klasse für das Erstellen von Hunden """

    def __init__(self, rufname, farbe, alter):
        """ Initalisieren über Eltern-Klasse """
        super().__init__(rufname, farbe, alter)

    def tut_reden(self, anzahl = 1):
        print("Bin Hund, rede nicht")
