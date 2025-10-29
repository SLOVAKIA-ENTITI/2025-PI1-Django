from django.shortcuts import render

def index(request):
    vysledok = ""
   
    if request.method == "POST":
        try:
            a = float(request.POST["a"])
            if a <= 1:
                prvocisloa = False
            else:
                prvocisloa = True
                for i in range(2, int(a)):
                    if a % i == 0:
                        prvocisloa = False
                        break

            if prvocisloa:
                vysledok = (f"{a} je prvočíslo")
            else:
                vysledok = (f"{a} nie je prvočíslo")

          

        except Exception as e:
            vysledok = f"Chyba: {e}"

    # 🔹 Render mimo try, aby sa vykonal vždy
    return render(request, 'prvocislo/index.html', {
        "vysledok": vysledok,

    })