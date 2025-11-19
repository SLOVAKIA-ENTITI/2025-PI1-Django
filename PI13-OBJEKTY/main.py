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


# dedičná trieda
class Ucitel(Osoba):  #dedičnosť -> Učiteľ zdeí všetky atribúty a metody od triedy osoba
    def __init__(self, meno, priezvisko, rok, titul, predmet, trieda):
        super().__init__(meno, priezvisko, rok) # použije konštruktor rodičovskej triedy
        self.titul = titul
        self.predmet = predmet
        self.trieda = trieda

    def pozdrav(self):
        print("Dobrý deň, som učiteľ", self.titul, self.meno, self.priezvisko, "a učím predmet", self.predmet)

class Student(Osoba):
    def __init__(self, meno, priezvisko, rok, trieda):
        super().__init__(meno, priezvisko, rok)
        self.trieda = trieda
    def pozdrav(self):
        print("Ahoj, volám sa", self.meno, self.priezvisko, "a som v triede", self.trieda)


# vytvorenie objektu
jano = Osoba("Ján", "Mrkvička", 2010)
jano.pozdrav()
jano.vypis_vek()


ucitel1 = Ucitel("Michal", "Šutek", 1978, "Mgr.", "ZCY", "IV.AT")
ucitel1.pozdrav()
ucitel1.vypis_vek()

student1 = Student("Matúš", "Paškala", 2008, "III.AT")
student1.pozdrav()
student1.vypis_vek()
