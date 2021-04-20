from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'nombre_app/index.html')

def formulario(request):
    return render(request, 'nombre_app/formulario.html')

def resultados(request):
    fname = request.POST['fname']
    lname = request.POST['lname']

    needs = []
    if 'need1' in request.POST: # OJO con los checkboxes
        needs.append(request.POST['need1'])
    if 'need2' in request.POST:  # OJO con los checkboxes
        needs.append(request.POST['need2'])
    if 'need3' in request.POST:  # OJO con los checkboxes
        needs.append(request.POST['need3'])

    nota = request.POST['nota']

    context = {}
    context['fname'] = fname
    context['lname'] = lname
    context['needs'] = needs
    context['nota'] = nota

    return render(request, 'nombre_app/resultados.html', context)