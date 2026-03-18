import re
from datetime import datetime
from django.shortcuts import render
from .models import Kruzok

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

    rad_od_teraz = request.GET.get('od_teraz') == '1'

    if rad_od_teraz:
        now = datetime.now()
        aktualny_den = now.weekday() + 1
        aktualny_cas = now.time()

        def sort_key_aktualne(kruzok):
            den_kruzku = zisti_najskorsi_den(kruzok.den)
            cas_kruzku = zisti_cas(kruzok.den) # Extrahuje čas z textu
            
            # Posun do ďalšieho týždňa, ak už krúžok bol
            if den_kruzku < aktualny_den or (den_kruzku == aktualny_den and cas_kruzku < aktualny_cas):
                rozdiel_dni = (den_kruzku - aktualny_den) + 7
            else:
                rozdiel_dni = den_kruzku - aktualny_den

            return (rozdiel_dni, cas_kruzku)

        vsetky_kruzky.sort(key=sort_key_aktualne)

    else:
        # Štandardné zoradenie - funkcia zavolá extrakciu dňa aj času pre každý objekt
        vsetky_kruzky.sort(key=lambda x: (zisti_najskorsi_den(x.den), zisti_cas(x.den)))

    return render(request, 'kruzky/index.html', {'kruzky': vsetky_kruzky})