import datetime


class Osoba:
    # konštruktor
    def __init__(self, meno, priezvisko, rok):
        self.meno = meno
        self.priezvisko = priezvisko
        self.rok = rok
        self.vek = datetime.date.today().year - self.rok
        # atribúty (vlastnosti)
    
    #metoda pozdrav
    def pozdrav(self):
        print("Ahoj ja som", self.meno, self.priezvisko)

    #metoda vypis vek
    def vypis_vek(self):
        print("Mám", self.vek, "rokov.")

    #stringová reprezentácia objektu, pri print() vypíš nasledovný string -> Meno Priezvisko
    def __str__(self):
        return f"{self.meno} {self.priezvisko}: Osoba"


# dedičná trieda
class Ucitel(Osoba):  #dedičnosť -> Učiteľ zdeí všetky atribúty a metody od triedy osoba
    def __init__(self, meno, priezvisko, rok, titul, predmet, trieda=None): # trieda=None znamená že atribút je nepovinný a defaultne bude none
        super().__init__(meno, priezvisko, rok) # použije konštruktor rodičovskej triedy
        self.titul = titul
        self.predmet = predmet
        self.trieda = trieda

    def pozdrav(self):
        if self.trieda:
            print("Dobrý deň, som učiteľ", self.titul, self.meno, self.priezvisko, "a učím predmet", self.predmet, "v triede", self.trieda)
        else:
            print("Dobrý deň, som učiteľ", self.titul, self.meno, self.priezvisko, "a učím predmet", self.predmet)


    def __str__(self):
        if self.trieda:
            return f"{self.titul} {self.meno} {self.priezvisko} - Učitel, Predmet: {self.predmet}: Trieda: {self.trieda}"
        else:
            return f"{self.titul} {self.meno} {self.priezvisko} - Učitel, Predmet: {self.predmet}"


class Student(Osoba):
    def __init__(self, meno, priezvisko, rok, trieda):
        super().__init__(meno, priezvisko, rok)
        self.trieda = trieda
    def pozdrav(self):
        print("Ahoj, volám sa", self.meno, self.priezvisko, "a som v triede", self.trieda)

    def __str__(self):
        return f"{self.meno} {self.priezvisko} - Študent, Trieda: {self.trieda}"





# vytvorenie objektu
jano = Osoba("Ján", "Mrkvička", 2010)
jano.pozdrav()
jano.vypis_vek()
print(jano)

ucitel1 = Ucitel("Michal", "Šutek", 1978, "Mgr.", "ZCY", "IV.AT")
ucitel1.pozdrav()
ucitel1.vypis_vek()
print(ucitel1)

student1 = Student("Matúš", "Paškala", 2008, "III.AT")
student1.pozdrav()
student1.vypis_vek()
print(student1)





import random

# Načítanie súborov
"""
with open("mena.txt","r",encoding="utf-8") as t:
    mena = []
    for riadok in t:
        meno = riadok.strip()
        mena.append(meno)

"""
with open('priezviska.txt', 'r', encoding='utf-8') as f:
    priezviska = [line.strip() for line in f if line.strip()]


with open('mena.txt', 'r', encoding='utf-8') as f:
    mena = [line.strip() for line in f if line.strip()]


trieda = ["A","B","C","D"]
rocnik = ["I.", "II.","III.","IV."]
rok = [2006, 2007, 2008, 2009]
titul = ["Mgr.", "Ing.", "PaeDr."]
predmet = ["ZCY","CPD","MAT","FYZ","SJL","PROG"]

# Opakovanie 10 krát

print("---------------------------------")
print("Žiaci:")
for i in range(10):
    priezvisko = random.choice(priezviska)
    meno = random.choice(mena)
    trieda_vyber = random.choice(trieda)
    rok_vyber = random.choice(rok)
    if rok_vyber == 2006:
        rocnik_vyber = "IV."
    elif rok_vyber == 2007:
        rocnik_vyber = "III."
    elif rok_vyber == 2008:
        rocnik_vyber = "II."
    else:
        rocnik_vyber = "I."

    trieda_vyber_spolu = f"{rocnik_vyber}{trieda_vyber}"


    student = Student(meno, priezvisko, rok_vyber, trieda_vyber_spolu)
    print(student)

print("---------------------------------")
print("Učitelia:")

triedy_pre_ucitelov = [
    "I.AI", "I.BI", "I.CI", "I.AT","I.AG",
    "II.AI", "II.BI", "II.CI", "II.AT","II.AG",
    "III.AI", "III.BI", "III.CI", "III.AT","III.AG",
    "IV.AI", "IV.BI", "IV.CI", "IV.AG", "IV.AT"
]

for i in range(10):
    priezvisko = random.choice(priezviska)
    meno = random.choice(mena)
    titul_vyber = random.choice(titul)
    predmet_vyber = random.choice(predmet)
    rok_vyber = random.choice(rok)

    trieda_ucitel = random.choice(triedy_pre_ucitelov)   
    triedy_pre_ucitelov.remove(trieda_ucitel)            

    ucitel = Ucitel(meno, priezvisko, rok_vyber, titul_vyber, predmet_vyber, trieda_ucitel)
    print(ucitel)
