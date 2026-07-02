from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login ,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Destination,save_destination
def home(request):
    return render(request,'home.html')
def admin_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_staff:
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,"sorry you'r not admin/staff")
                return redirect('login')
        else:
           messages.error(request,'please check password | username')
           return redirect('Admin')
    return render(request,'admin.html')
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'login successfull')
            return redirect('home')
        else:
           messages.error(request,'please check the details properly')
           return redirect('login')
    return render(request,'user.html')
def logout_view(request):
    logout(request)
    return redirect('login')
def register_view(request):
    if request.method =='POST':
        First_Name = request.POST['name']
        Email=request.POST['email']
        username =request.POST['username']
        password =request.POST['password']
        confirmation_password =request.POST['cnfrm_password']
        select_user=request.POST['select_user']
        if select_user == 'admin':
            select_user=True
        else :
            select_user=False
        if password == confirmation_password:
            user = User.objects.filter(username=username)
            if user:
                messages.error(request,'username already exist use different')
                return redirect('register')
            else:
                user=User.objects.create_user(
                    username=username,
                    password=password,
                    email=Email,
                    first_name=First_Name,is_staff=select_user)
                user.save()
                messages.success(request,'created account successfully')
                return redirect('login')
        else:
            messages.error(request,'password should same password twice')
            return redirect('register')
    return render(request,'register.html')
def dashboard_view(request):
    data=Destination.objects.all()
    return render(request,'travel.html',{'destinations':data})
def Udashboard_view(request):
    if request.method=='POST':
        budget=request.POST['budget']
        duration=request.POST['duration']
        Season=request.POST['season']
        data=Destination.objects.filter(Duration=duration,Season=Season ,budget=budget)
        return render(request,'Utravel.html',{'destinations':data})
    return render(request,'Utravel.html')
def add_destination(request):
    if request.method=='POST':
        Name=request.POST['destinationName']
        budget=request.POST['budget']
        Duration=request.POST['duration']
        Season=request.POST['season']
        activate=request.POST['activities']
        data=Destination.objects.create(Name=Name,budget=budget,Duration=Duration,Season=Season,activate= activate)
        data.save()
        return redirect('Adashboard')
    return redirect('Adashboard')
def save_Destination(request,pk):
        destination=Destination.objects.get(id=pk)
        data=save_destination.objects.filter(user=request.user,destination=destination)
        if data:
            return redirect('udashboard')
        else:
            data=save_destination.objects.create(user=request.user,destination=destination)
            data.save()
            return redirect('udashboard')
        return redirect('udashboard')
def saved_list(request):
    data=save_destination.objects.filter(user=request.user)
    return render(request,"savelist.html",{'destinations':data})
def delete_saved(request,pk):
    data=save_destination.objects.get(id=pk)
    data.delete()
    return redirect('Save_list')
def delete_destionation(request,pk):
    data=Destination.objects.get(id=pk)
    data.delete()
    return redirect('Adashboard')