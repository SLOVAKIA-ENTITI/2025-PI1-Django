from django.shortcuts import render

def index(request):
    # 🔹 Inicializácia premenných – budú existovať vždy
    vysledok = ""
    apar = ""
    bpar = ""
    aprv = ""
    bprv = ""

    if request.method == "POST":
        try:
            a = float(request.POST["a"])
            b = float(request.POST["b"])

            # Ktoré číslo je väčšie
            if a > b:
                vysledok = a
            elif b > a:
                vysledok = b
            else:
                vysledok = "Čísla sa rovnajú"

            # Párnosť
            if a % 2 == 0:
                apar = "Číslo A je párne"
            else:
                apar = "Číslo A je nepárne"

            if b % 2 == 0:
                bpar = "Číslo B je párne"
            else:
                bpar = "Číslo B je nepárne"

            # Prvočíslo A
            if a <= 1:
                prvocisloa = False
            else:
                prvocisloa = True
                for i in range(2, int(a)):
                    if a % i == 0:
                        prvocisloa = False
                        break

            if prvocisloa:
                aprv = "Číslo A je prvočíslo."
            else:
                aprv = "Číslo A nie je prvočíslo."

            # Prvočíslo B
            if b <= 1:
                prvocislob = False
            else:
                prvocislob = True
                for i in range(2, int(b)):
                    if b % i == 0:
                        prvocislob = False
                        break

            if prvocislob:
                bprv = "Číslo B je prvočíslo."
            else:
                bprv = "Číslo B nie je prvočíslo."

        except Exception as e:
            vysledok = f"Chyba: {e}"

    # 🔹 Render mimo try, aby sa vykonal vždy
    return render(request, 'cisla_app/index.html', {
        "vysledok": vysledok,
        "apar": apar,
        "bpar": bpar,
        "aprv": aprv,
        "bprv": bprv
    })
