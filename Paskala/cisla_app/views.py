from django.shortcuts import render

def index(request):
    if request.method == "GET":
        vysledok = 0
        apar = " "
        bpar = " "
        aprv = " "
        brpv = " "
    if request.method == "POST":
        try:
            a = float(request.POST["a"])
            b = float(request.POST["b"])
            if a > b:
                vysledok = a 
            elif b > a:
                vysledok = b
            else:
                vysledok = "Čísla sa rovnajú"

            if a % 2 == 0:
                apar = "Číslo A je párne"
            else:
                apar = "číslo A je nepárne"

            if b % 2 == 0:
                bpar = "Číslo B je párne"
            else:
                bpar = "číslo B je nepárne"

           


        except:
            vysledok = "Chyba"


    return render(request, 'cisla_app/index.html', {"vysledok":vysledok, "apar":apar, "bpar":bpar, "aprv":aprv} )
