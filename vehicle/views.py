from django.shortcuts import render,redirect
from .forms import VehicleForm
from .models import Vehicles
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='login')
def Vehicle_list(request):
    context = {'vehicle_list': Vehicles.objects.all()}
    return render(request, "vehicleList.html", context)

@login_required(login_url='login')
def Vehicle_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = VehicleForm()
        else:
            vehicle = Vehicles.objects.get(pk=id)
            form = VehicleForm(instance=vehicle)
        return render(request, "vehicleform.html", {'form': form})
    else:
        if id == 0:
            form = VehicleForm(request.POST)
        else:
            vehicle = Vehicles.objects.get(pk=id)
            form = VehicleForm(request.POST,instance= vehicle)
        if form.is_valid():
            form.save()
        return redirect('list')

@login_required(login_url='login')
def vehicle_delete(request,id):
    employee = Vehicles.objects.get(pk=id)
    employee.delete()
    return redirect('list')