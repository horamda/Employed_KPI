from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Personal, Indicador

@login_required
def perfil(request):
    personal = Personal.objects.get(user=request.user)
    indicadores = Indicador.objects.filter(personal=personal)
    return render(request, 'dashboard/perfil.html', {'personal': personal, 'indicadores': indicadores})

@login_required
def dashboard(request):
    personal = Personal.objects.get(user=request.user)
    indicadores = Indicador.objects.filter(personal=personal)
    return render(request, 'dashboard/dashboard.html', {'personal': personal, 'indicadores': indicadores})

@login_required
def cargar_csv(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']
        reader = csv.reader(csv_file)
        for row in reader:
            personal = Personal.objects.get(id=row[0])
            kpi = KPI.objects.get(id=row[1])
            valor = row[2]
            fecha = row[3]
            Indicador.objects.create(personal=personal, kpi=kpi, valor=valor, fecha=fecha)
        return HttpResponse('Datos cargados exitosamente')
    return render(request, 'dashboard/cargar_csv.html')
