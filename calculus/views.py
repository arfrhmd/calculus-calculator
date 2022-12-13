from django.shortcuts import render
from django.http import HttpResponse
import logic.math as math_calc
import json

# Create your views here.
def calculus(request):
    return render(request, "index.html")

def calculate(request):
    if request.method == 'POST':
        formula = request.POST['formula']
        if request.POST['formula-option'] == '1':
            data = math_calc.basic_derivative(formula)
            store_json = json.dumps(data)
            return HttpResponse(store_json)
        elif request.POST['formula-option'] == '2':
            data = math_calc.basic_derivative(formula)
            store_json = json.dumps(data)
            return HttpResponse(store_json)
        elif request.POST['formula-option'] == '3':
            data = math_calc.quadratic_equation(formula)
            store_json = json.dumps(data)
            return HttpResponse(store_json)
    else:
        data = {
            "formula": None,
            "result": None
        }
        store_json = json.dumps(data)
        return HttpResponse(store_json)