from django import forms
from .models import Check, Book, Contact
from django.db import models
from django import forms

class CheckForm(forms.ModelForm):
    date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Check
        fields = ('farmhouse_Name','date', 'Day_or_Night',)

class BookForm(forms.ModelForm):
    date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Book
        fields = ('Your_Name','farmhouse_Name', 'Number_Of_People','date', 'Day_or_Night','Contact')
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('Name', 'Email','Subject', 'Message',)
