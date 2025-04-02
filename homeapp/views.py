from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    #return HttpResponse("<h1>Hello all</h1>")
    return render (request, "home.html", {})

def add_emp(request):
    if request.method=='POST':
        emp_id=request.POST.get('emp_id')
        name=request.POST.get('name')
        contact=request.POST.get('contact')
        dept=request.POST.get('dept')
        jdate=request.POST.get('jdate')
        add=request.POST.get('add')
        state=request.POST.get('state')
        idproof=request.POST.get('idproof')

        print(emp_id, name, contact, dept, jdate, add, zip, state, idproof)

        e=Empdata()
        e.emp_id=emp_id
        e.name=name
        e.contact=contact
        e.dept=dept
        e.jdate=jdate
        e.add=add
        e.state=state
        e.idproof=idproof

        e.save()
    
    return render(request, "add_emp.html", {})


def emp_list(request):
    empdata=Empdata.objects.all()

    return render(request, "emplist.html", {'empdata':empdata})

def emp_detail(request, id):
    empinfo=Empdata.objects.get(pk=id)

    return render(request, "emp_detail.html", {'emp':empinfo})

def emp_update(request, id):
    empinfo=Empdata.objects.get(pk=id)

    return render(request, "emp_update.html", {'emp':empinfo})


def do_emp_update(request, id):

    if request.method=='POST':
        name=request.POST.get('name')
        contact=request.POST.get('contact')
        dept=request.POST.get('dept')
        jdate=request.POST.get('jdate')
        ldate=request.POST.get('ldate')
        add=request.POST.get('add')
        state=request.POST.get('state')
        idproof=request.POST.get('idproof')
        working=request.POST.get('working')

        e=Empdata.objects.get(pk=id)
        e.name=name
        e.contact=contact
        e.dept=dept
        e.jdate=jdate
        e.ldate=ldate
        e.add=add
        e.state=state
        e.idproof=idproof

        if working is None:
            e.working=False
        else:
            e.working=True
        
        e.save()

    # render to the employee details page to see changes
    empdata=Empdata.objects.all()
    return render(request, "emplist.html", {'empdata':empdata})

