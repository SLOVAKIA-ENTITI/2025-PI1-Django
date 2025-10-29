from django.shortcuts import render
from datetime import date

def index(request):
    a = 0
    vysledok = 0
    den = 0
    mesiac = 0
    rok = 0
    if request.method == "POST":
        try:
            a = str(request.POST["meno"])
            datum = str(request.POST["date"])
            vysledok = 0
            def calculateAge(birthDate):
                today = date.today()
                age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))

                return age
            
            den = datum[:2]
            den = int(den)
            mesiac = datum[2:4]
            mesiac = int(mesiac)
            rok = datum[4:8]
            if mesiac == 1:
                mesiac = "Január"
            elif mesiac == 2:
                mesiac = "Február"
            elif mesiac == 3:
                mesiac = "Marec"
            elif mesiac == 4:
                mesiac = "Apríl"
            elif mesiac == 5:
                mesiac = "Máj"
            elif mesiac == 6:
                mesiac = "Jún"
            elif mesiac == 7:
                mesiac = "Júl"
            elif mesiac == 8:
                mesiac = "August"
            elif mesiac == 9:
                mesiac = "September"
            elif mesiac == 10:
                mesiac = "Október"
            elif mesiac == 11:
                mesiac = "November"
            elif mesiac == 12:
                mesiac = "December"
            elif mesiac > 12:
                mesiac = "Neexistujúci mesiac"


            vysledok = (f"Ahoj {a} tvoj dátum narodenia je: {den}. {mesiac} {rok}.")
            if den > 31 or mesiac == "Neexistujúci mesiac":
                vysledok = "Chyba!!!!!"
            else:
                vysledok = (f"Ahoj {a} tvoj dátum narodenia je: {den}. {mesiac} {rok}.")
            
            
        except Exception as e:
            vysledok = f"Chyba: {e}"
    return render(request, 'vek/index.html', {"vysledok": vysledok, "den": den, "mesiac": mesiac, "rok": rok,})