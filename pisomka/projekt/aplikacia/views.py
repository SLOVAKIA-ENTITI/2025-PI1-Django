from django.shortcuts import render

def index(request):
    vysledok = 0
    cislo = 0
    if request.method == "POST":
        try:
            cislo = float(request.POST["cislo"])
            def faktorial(a):
                if a == 0:
                    return 1
                else :
                    return a * faktorial(a - 1)
                
            vysledok = (f"Faktoriál čísla je: {faktorial(cislo)}")
        except Exception as e:
            vysledok = f"Chyba: {e}"
    return render(request, 'aplikacia/index.html', {"vysledok": vysledok,})
