from django.shortcuts import render

def index(request):
    a = 0
    vysledok = 0
    if request.method == "POST":
        try:
            a = str(request.POST["a"])
            b = map(int, str(a))
            vysledok = 0

            for cislo in b:
                vysledok = vysledok + cislo
        
            
        except Exception as e:
            vysledok = f"Chyba: {e}"
    return render(request, 'ciferny_sucet/index.html', {"vysledok": vysledok,})