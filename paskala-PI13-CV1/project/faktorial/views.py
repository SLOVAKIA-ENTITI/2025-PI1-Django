from django.shortcuts import render

def index(request):
    vysledok = 0
    a = 0
    if request.method == "POST":
        try:
            a = float(request.POST["a"])
            def faktorial(a):
                if a == 0:
                    return 1
                else :
                    return a * faktorial(a - 1)
                
            vysledok = (f"Faktoriál čísla je: {faktorial(a)}")
        except Exception as e:
            vysledok = f"Chyba: {e}"
    return render(request, 'faktorial/index.html', {"vysledok": vysledok,})