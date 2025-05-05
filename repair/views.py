from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Repairtable
from vehicle.models import Vehicle
from .forms import RepairForm
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        form=RepairForm()
        return render(request,'repair/index.html',{'form':form})
    else:
        return redirect("/home/404")



def repair(request):
    if request.method == 'POST':
        vehicle_id = request.POST.get('vehicle')
        issue = request.POST.get('issue')
        vehicle = Vehicle.objects.get(id=vehicle_id)
        print("dfgdf",vehicle)
        user = request.user
        repairtable = Repairtable(vehicle=vehicle, issue=issue, registeredUser=user)
        repairtable.save()
        return redirect('issues')
    else:
        user = request.user
        vehicles = Vehicle.objects.filter(owner=user)
        context = {'vehicles': vehicles}
        return render(request, 'repair/add_issue.html', context)

def issues(request):
    if request.POST:
        form=RepairForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.registeredUser=request.user
            instance.save()
            success_message='Issue Registered'
            
        return render(request,'repair/index.html',{'form':form})
    else:
        if request.user.is_authenticated:
            repairsList = Repairtable.objects.filter(registeredUser=request.user)
            return render(request,'repair/issues.html',{ 'repairsList' : repairsList})
        else:
            return redirect("/home/404")

def update(request,id):
    if request.POST:
        # form=RepairForm(request.POST)
        # if form.is_valid():
        #     instance=form.save(commit=False)
        #     instance.registeredUser=request.user
        #     instance.save()
        #     success_message='Issue Registered'
        #     form=RepairForm()
        return render(request,'repair/index.html',{'form':form})
    else:
        if request.user.is_authenticated:
            repair = Repairtable.objects.get(id=id)
            if repair.status == "S":
                repair.status = "NS"
            else:
                repair.status = "S"
            repair.save()
            repairsList = Repairtable.objects.all()
            return redirect('/repair/issues')
        else:
            return redirect("/home/404")

def edit(request,id):
    if request.method == "POST":
        repair=Repairtable.objects.get(id=id)
        form=RepairForm(request.POST,instance=repair)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('/repair/issues')
    elif request.user.is_authenticated:
        repair=Repairtable.objects.get(id=id)
        form=RepairForm(instance=repair)
        return render(request,'repair/repairEdit.html',{ 'form' : form ,'id':id})