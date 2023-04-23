from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse

from emp.models import employee
# Create your views here.

def home(request):
        emps=employee.objects.all()
        return render(request ,"index.html", {'emps':emps})
    
def add_emp(request):
    if request.method=='POST':


# fetch Data 

        emp_name=request.POST.get('emp_name')
        emp_email=request.POST.get('emp_email')
        emp_phone=request.POST.get('emp_Phone')
        emp_working=request.POST.get('emp_working')
        emp_address=request.POST.get('emp_address')
# create a model object to set data 

        e=employee()
        e.name=emp_name
        e.Email=emp_email
        e.phone=emp_phone
        e.address=emp_address
        if emp_working is None:
                e.working = False
        else:
            e.working=True

    # saveing the Object
        e.save()
    
        return redirect("/emp/")
    return  render( request ,"add_emp.html")

def delete_emp(request,emp_id):
        emp = employee.objects.get(pk=emp_id)
        emp.delete()
        return redirect("/emp/")   

def update_emp(request,emp_id):
        upemp = employee.objects.get(pk=emp_id)
        return render( request ,'update_emp.html' , {'upemp':upemp})    

def do_update(request,emp_id):
        if request.method=='POST':
                emp_name=request.POST.get('emp_name')
                emp_email=request.POST.get('emp_email')
                emp_phone=request.POST.get('emp_Phone')
                emp_working=request.POST.get('emp_working')
                emp_address=request.POST.get('emp_address')
        e = employee.objects.get(pk=emp_id)

        e.name=emp_name
        e.Email=emp_email
        e.phone=emp_phone
        e.address=emp_address
        if emp_working is None:
                e.working = False
        else:
                e.working=True

        e.save()

        return redirect("/emp/")           