from django.shortcuts import render

def index(request):
    if request.method == "GET":
        vysledok = 0
    if request.method == "POST":
        try:
            a = float(request.POST["a"])
            b = float(request.POST["b"])
            operator = request.POST["operator"]
            if operator == "+":
                vysledok = a + b
            elif operator == "-":
                vysledok = a - b
            elif operator == "*":
                vysledok = a * b
            else:
                vysledok = a / b
        except ZeroDivisionError:
            vysledok = "Nemozes delit nulov"
        except ValueError:
            vysledok = "Zadávaj len čísla"
        except:
            vysledok = "Chyba"


    return render(request, 'kalkulacka/index.html', {"vysledok": vysledok} )
