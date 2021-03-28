from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import BookingList
from .forms import BookingListForm
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


def book(request):
    if request.method=="POST":
        form=BookingListForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=BookingListForm()
    return render(request,"myapp/book.html",{"form":form})