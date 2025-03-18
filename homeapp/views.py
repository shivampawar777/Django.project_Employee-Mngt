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
        fname=request.POST.get('fname')
        mname=request.POST.get('mname')
        lname=request.POST.get('lname')
        dept=request.POST.get('dept')
        add=request.POST.get('add')
        zip=request.POST.get('zip')
        state=request.POST.get('state')
        idproof=request.POST.get('idproof')
        working=request.POST.get('working')

        print(emp_id,fname, mname,lname, dept, add, zip, state, idproof, working)

        e=Emp_add()
        e.emp_id=emp_id
        e.fname=fname
        e.mname=mname
        e.lname=lname
        e.dept=dept
        e.add=add
        e.zip=zip
        e.state=state
        e.idproof=idproof

        if working is None:
            e.working=False
        else:
            e.working=True

        e.save()
        e.delete()

    return render (request, "add_emp.html", {})