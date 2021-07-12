# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .forms import CheckForm, BookForm, ContactForm
from .models import *
# Create your views here.
def landing(request):
    
    return render(request, 'landing.html', {})



def home(request):
    checkform = CheckForm()
    bookform = BookForm()
    contactform = ContactForm()
    respond1 = 'Check Availibility'
    respond2 = 'Book My Farm'
    
    return render(request, 'index.html', {'respond3' :'Send Message','contactform': contactform,'checkform': checkform, 'bookform': bookform, "checkactive" :'active','showactivecheck':'show active', "respond1":respond1, "respond2":respond2})

def booked(request):
    checkform = CheckForm()
    bookform = BookForm()
    contactform = ContactForm()
    respond1 = "Check Availibility"
    respond2 = 'Book My Farm'
    if request.method=="POST":
        data=BookForm(request.POST)
        if data.is_valid():
            print(request.POST.get('date'))
            checkbooking = Book.objects.filter(date=request.POST.get('date')).count()
            
            if checkbooking>0:
                respond2 = 'We have Booked Your Farm But it seems like we have another reservation. Our Team will confirm you shortly!'
            else:
                respond2='You Have Booked the Farm For You, Our Team Will Contact You Shortly!'
            data.save()
            return render(request,'index.html',{'respond3' :'Send Message','contactform':contactform,'checkform': checkform,  'respond1':respond1, 'respond2':respond2,"bookactive" :'active','showactivebook':'show active',})
        else:
            data=bookform
            respond2='Farm Has Not Been Booked, Please try Again!'
            return render(request,'index.html',{'respond3' :'Send Message','contactform': contactform,'checkform': checkform,'data':data, 'respond1':respond1, 'respond2':respond2,"bookactive" :'active','showactivebook':'show active',})
    return render(request, 'index.html', {'respond3' :'Send Message','contactform': contactform,'checkform': checkform, 'bookform': bookform, 'respond1':respond1, 'respond2':respond2,"checkbook" :'active','showactivebook':'show active',})


def checked(request):
    checkform = CheckForm()
    bookform = BookForm()
    contactform = ContactForm()
    respond1 = "Check Availibility"
    respond2 = 'Book My Farm'
    if request.method=="POST":
        data=CheckForm(request.POST)
        if data.is_valid():
            print(request.POST.get('date'))
            checkbooking = Book.objects.filter(date=request.POST.get('date'), Day_or_Night= request.POST.get('Day_or_Night')).count()
            
            if checkbooking>0:
                respond1 = 'Not Available, please try some other Date! (Click Me To Try Again)'
            else:
                respond1='Available on you Preferred Date, Click on the next tab to Book it now!'
            # data.save()
            return render(request,'index.html',{'respond3' :'Send Message','contactform':contactform,'checkform':checkform,'bookform':bookform,  'respond1':respond1, 'respond2':respond2,"checkactive" :'active','showactivecheck':'show active',})
        else:
            data=checkform
            respond2='Please Re-Enter your Preferred Date!'
            return render(request,'index.html',{'respond3' :'Send Message','contactform':contactform,'checkform': checkform,'bookform':bookform,'data':data, 'respond1':respond1, 'respond2':respond2,'checkactive' :'active','showactivecheck':'show active',})
    return render(request, 'index.html', {'respond3' :'Send Message','contactform':contactform,'checkform': checkform, 'bookform': bookform, 'respond1':respond1, 'respond2':respond2,"checkactive" :'active','showactivecheck':'show active',})


def contacted(request):
    checkform = CheckForm()
    bookform = BookForm()
    contactform = ContactForm()
    respond1 = 'Check Availibility'
    respond2 = 'Book My Farm'
    respond3 ='Send Message',
    if request.method=="POST":
        data=ContactForm(request.POST)
        if data.is_valid():
            data.save()
            respond3='Your Message has been sent successfully!'
            return render(request, 'index.html', {'checkform': checkform, 'bookform': bookform, "checkactive" :'active','showactivecheck':'show active', "respond1":respond1, "respond2":respond2, 'respond3':respond3})

        else:
            data=Messages()
            respond3='Your Message has been sent successfully!'
            return render(request, 'index.html', {'checkform': checkform, 'bookform': bookform, "checkactive" :'active','showactivecheck':'show active', "respond1":respond1, "respond2":respond2, 'respond3':respond3})

    return render(request, 'index.html', {'contactform': contactform,'checkform': checkform, 'bookform': bookform, "checkactive" :'active','showactivecheck':'show active', "respond1":respond1, "respond2":respond2, 'respond3':respond3})

