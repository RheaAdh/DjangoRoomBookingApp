from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import BookingList,AdminEditList
from .forms import BookingListForm,AdminEditListForm
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib.admin.views.decorators import staff_member_required

def mainpage(request):
    return render(request,'myapp/main.html')

def featurespage(request):
    return render(request,'myapp/features.html')
    
@staff_member_required
def index(request):
    bookings=BookingList.objects.all()
    return render(request,"myapp/index.html",{"bookings":bookings})

@login_required
def book(request):
    if request.method=="POST":
        form=BookingListForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form=BookingListForm()
    return render(request,"myapp/book.html",{"form":form})

@staff_member_required
def edit(request):
    if request.method=="POST":
        form=AdminEditListForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=AdminEditListForm()
    return render(request,"myapp/edit.html",{"form":form})