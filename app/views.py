from django.shortcuts import render,redirect
from .models import Students
from django.contrib import messages
from app.forms import StudentForm

def index(request):
    fm=   fm = Students.objects.all()
    return render(request, 'app/index.html',{'fm':fm})

def add_record(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            form = StudentForm()
            messages.success(request,"Add Record Successfuly")
    else:
        form = StudentForm()
    return render(request, 'app/addrecord.html', {'form': form})


# show data logic

def show(request):
    fm = Students.objects.all()
    return render(request, 'app/show.html',{'fm':fm})

# delete students record.......


def delete(request,id):
    fm = Students.objects.get(pk=id)
    fm.delete()
    messages.info(request,"Delet Record")
    return redirect('show')

# update students  records......................


def update(request,id):
    if request.method=='POST':
        p=Students.objects.get(id=id)
        fm=StudentForm(request.POST,instance=p)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Record Updated ")
            return redirect('show')

    else:
        p = Students.objects.get(id=id)
        fm = StudentForm(instance=p)
    return render(request,'app/update.html',{'fm':fm})


def adm_panel(request):
    fm = Students.objects.all().count()
    return render(request,'app/admin.html',{'fm':fm,})

def pie_chart(request):
    labels = []
    data = []

    queryset = Students.objects.order_by('-name')
    for city in queryset:
        labels.append(Students.name)
        data.append(Students.address)

    return render(request, 'app/char.html', {
        'labels': labels,
        'data': data,
    })


