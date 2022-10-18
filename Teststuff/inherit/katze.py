from teststuff.inherit.tier import Tier

class BauplanKatzenKlasse(Tier):
    """ Klasse für das Erstellen von Katzen """

    def __init__(self, rufname, farbe, alter):
        """ Initalisieren über Eltern-Klasse """
        super().__init__(rufname, farbe, alter)

