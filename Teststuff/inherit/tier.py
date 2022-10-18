class Tier():
    """ Klasse für das Erstellen von Säugetieren """

    def __init__(self, rufname, farbe, alter):
        self.rufname = rufname
        self.farbe   = farbe
        self.alter   = alter
        self.schlafdauer = 0

    def tut_schlafen(self, dauer):
        print(self.rufname, " schläft jetzt ", dauer , " Minuten ")
        self.schlafdauer += dauer
        print(self.rufname, " Schlafdauer insgesamt: ", self.schlafdauer, " Minuten ")

    def tut_reden(self, anzahl = 1):
        print(self.rufname, "sagt: ", anzahl * "miau ")
