from django.shortcuts import render
from nombre_app.forms import Formulario

# Create your views here.
def index(request):
    return render(request, 'nombre_app/index.html')

def formulario(request):
    form = Formulario()
    return render(request, 'nombre_app/formulario.html', {'form': form})

def resultados(request):
    fname = request.POST['fname']
    lname = request.POST['lname']

    needs = []
    if 'need1' in request.POST: # OJO con los checkboxes
        needs.append("sueño")
    if 'need2' in request.POST:  # OJO con los checkboxes
        needs.append("hambre")
    if 'need3' in request.POST:  # OJO con los checkboxes
        needs.append("tristeza")

    nota = request.POST['nota']

    context = {}
    context['fname'] = fname
    context['lname'] = lname
    context['needs'] = needs
    context['nota'] = nota

    return render(request, 'nombre_app/resultados.html', context)