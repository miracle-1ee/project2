from django.shortcuts import render, redirect
from django import forms
from .models import cal
from django.http import HttpResponse
from app01 import models
# Create your views here.

def index(request):
    return render(request,'index.html')

def CalPage(request):
    return render(request,'cal.html')

def Cal(request):
    if request.POST:

        value_a=request.POST['valueA']
        value_b=request.POST['valueB']
        result=int(value_a)+int(value_b)
        cal.objects.create(value_a=value_a,value_b=value_b,result=result)

        return render(request,'result.html',context={'data':result})
    else:
        return HttpResponse('Please visit us with POST')
def CalList(request):
    data=cal.objects.all()
    # for data in data:
    #     print(data.value_a,data.value_b,data.result)
    return render(request,'list.html',context={'data':data} )

def DelData(request):
    cal.objects.all().delete()
    return HttpResponse('data Deleted')


def info_list(request):
    print(1)
    data_list=models.UserInfo.objects.all()
    for obj in data_list:
        print(obj.name)
    print(data_list)

    return render(request,"info_list.html",context={'data_list':data_list})

def info_add(request):
    if request.method == "GET":
        return render(request,'info_add.html')

    user=request.POST.get("user")
    pwd=request.POST.get("pwd")
    age=request.POST.get("age")

    models.UserInfo.objects.create(name=user,password=pwd,age=age)
    return redirect("/info/list/")

def info_delete(request):
    nid=request.GET.get('nid')
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect("/info/list/")

def depart_list(request):
    '''部门列表'''

    queryset=models.Department2.objects.all()


    return render(request,'depart_list.html',context={'queryset':queryset})

def depart_add(request):
    '''添加部门'''

    if request.method == 'GET':
        return render(request,'depart_add.html')

    title=request.POST.get("title")

    models.Department2.objects.create(title=title)
    return redirect("/depart/list/")

def depart_delete(request):
    nid=request.GET.get('nid')
    models.Department2.objects.filter(id=nid).delete()
    return redirect("/depart/list/")

def depart_edit(request,nid):


    if request.method == 'GET':
        row_obj = models.Department2.objects.filter(id=nid).first()
        return render(request,'depart_edit.html',context={'row_obj':row_obj})

    title=request.POST.get("title")
    models.Department2.objects.filter(id=nid).update(title=title)
    return redirect("/depart/list")

def user_list(request):

    queryset=models.UserInfo2.objects.all()
    return render(request,"user_list.html",context={'queryset':queryset})

class UserModelForm(forms.ModelForm):
    class Meta:
        model=models.UserInfo2
        fields=["name","password","age","account","create_time","gender","depart"]
        # widgets={
        #     "name":forms.TextInput(attrs={"class":"form-control"}),
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name,field in self.fields.items():
            print(name,field)
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}


def user_add(request):

    if request.method=="GET":
        form=UserModelForm()
        return render(request,'user_add.html',context={'form':form})

    form=UserModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return  redirect("/user/list/")

    return render(request, 'user_add.html', context={'form': form})



