import re
from datetime import datetime
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, redirect
from .models import Kruzok
from .forms import PrihlaskaForm 
from .forms import KruzokForm

PORADIE_DNI = {
    'pondelok': 1,
    'utorok': 2,
    'streda': 3,
    'štvrtok': 4,
    'piatok': 5,
    'sobota': 6,
    'nedeľa': 7
}

def zisti_najskorsi_den(den_string):
    """Nájde všetky dni v textovom reťazci a vráti číselnú hodnotu najskoršieho."""
    if not den_string:
        return 99

    den_string = den_string.lower()
    najdene_hodnoty = []

    for den, cislo in PORADIE_DNI.items():
        if den in den_string:
            najdene_hodnoty.append(cislo)

    return min(najdene_hodnoty) if najdene_hodnoty else 99

def zisti_cas(den_string):
    """Vyhľadá v texte čas vo formáte HH:MM a vráti ho ako time objekt."""
    if not den_string:
        return datetime.strptime('00:00', '%H:%M').time()

    # Regulárny výraz hľadá čísla vo formáte napr. 16:00 alebo 8:30
    match = re.search(r'\d{1,2}:\d{2}', den_string)
    
    if match:
        najdeny_cas_text = match.group()
        try:
            return datetime.strptime(najdeny_cas_text, '%H:%M').time()
        except ValueError:
            pass # Ak by bol formát neplatný (napr. 25:99), ignorujeme to
            
    # Ak sa v texte žiadny čas nenájde, priradíme mu štandardný (napr. polnoc)
    return datetime.strptime('00:00', '%H:%M').time()


def zoznam_kruzkov(request):
    vsetky_kruzky = list(Kruzok.objects.all())
    
    # PRidaný výpočet vedúcich (pôvodne bol v inej funkcii)
    pocet_veducich = Kruzok.objects.values('veduci').distinct().count()

    rad_od_teraz = request.GET.get('od_teraz') == '1'

    if rad_od_teraz:
        now = datetime.now()
        # ... tvoj kód pre zoradenie od teraz ...
        def sort_key_aktualne(kruzok):
            den_kruzku = zisti_najskorsi_den(kruzok.den)
            cas_kruzku = zisti_cas(kruzok.den)
            if den_kruzku < (now.weekday() + 1) or (den_kruzku == (now.weekday() + 1) and cas_kruzku < now.time()):
                rozdiel_dni = (den_kruzku - (now.weekday() + 1)) + 7
            else:
                rozdiel_dni = den_kruzku - (now.weekday() + 1)
            return (rozdiel_dni, cas_kruzku)

        vsetky_kruzky.sort(key=sort_key_aktualne)
    else:
        vsetky_kruzky.sort(key=lambda x: (zisti_najskorsi_den(x.den), zisti_cas(x.den)))

    # Posielame kruzky AJ pocet_veducich v jednom balíku (context)
    return render(request, 'kruzky/index.html', {
        'kruzky': vsetky_kruzky,
        'pocet_veducich': pocet_veducich
    })




def prihlaska_view(request):
    initial = {}

    # z URL: ?kruzok=ID
    kruzok_id = request.GET.get('kruzok')
    if kruzok_id:
        initial['kruzok'] = kruzok_id

    form = PrihlaskaForm(request.POST or None, initial=initial)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('success')

    return render(request, 'kruzky/prihlaska.html', {
        'form': form
    })
def pridat_kruzok_view(request):
    form = KruzokForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('zoznam_kruzkov')

    return render(request, 'kruzky/pridat_kruzok.html', {'form': form})


def success_view(request):
    return render(request, 'kruzky/success.html')

def zmazat_kruzok(request, id):
    kruzok = get_object_or_404(Kruzok, id=id)
    kruzok.delete()
    return redirect('zoznam_kruzkov')