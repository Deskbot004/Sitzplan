from teststuff.inherit import hund, katze


tier = hund.Hund("Bello", "Gelb", 3)
tier2 = katze.BauplanKatzenKlasse("Nia", "Weiß", 5)


print(tier.redet)
tier.tut_reden(3)
tier2.tut_reden(3)
print(tier.redet)