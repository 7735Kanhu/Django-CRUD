from django.shortcuts import render
from home.models import *
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
def home(request):
    return render(request,"base.html")

def show(request):
    data = Entry.objects.all()
    return render(request,"show.html",{'data':data})
def send(request):
    if request.method == 'POST':
        id = request.POST['id']
        data1 = request.POST['data1']
        data2 = request.POST['data2']
        Entry(id=id,data1=data1,data2=data2).save()
        msg = "Data Stored Sucessfully"
        return render(request,'base.html',{'msg':msg})
    else:
        return HttpResponse("Error 404- Page not found")
    
    
def delete(request):
    id = request.GET['id']
    Entry.objects.filter(id=id).delete()
    return HttpResponseRedirect("show")


def edit(request):
    id = request.GET['id']
    data1 = data2 = 'NULL'
    for data in Entry.objects.filter(id = id):
        data1 = data.data1
        data2 = data.data2
    return render(request,"edit.html",{'id':id,'data1':data1,'data2':data2})        
        
        
def editrecord(request):
    if request.method == 'POST':
        id = request.POST['id']
        data1 = request.POST['data1']
        data2 = request.POST['data2']
        Entry.objects.filter(id = id).update(data1=data1,data2=data2)
        msg = "Data Update Sucessfull"
        return HttpResponseRedirect("show",{'msg':msg})