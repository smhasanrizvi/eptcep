from django.db import models

# Create your models here.
class Check(models.Model):
    farms = (
        ('Maple', 'Maple'),
        
    )
    farmhouse_Name = models.CharField(max_length=100, choices=farms ,default='Maple')
    
    CHOICES = (
        ('Day', 'Day'),
        ('Night', 'Night'),
    )
    date=models.DateField()
    Day_or_Night=models.CharField(max_length=100, choices = CHOICES)
    
class Book(models.Model):
    farms = (
        ('Maple', 'Maple'),
        
    )
    Your_Name = models.CharField(max_length=100, default='')
    farmhouse_Name = models.CharField(max_length=100, choices=farms ,default='Maple')
    Number_Of_People = models.IntegerField(null=True)
    CHOICES = (
        ('Day', 'Day'),
        ('Night', 'Night'),
    )
    date=models.DateField()
    Day_or_Night=models.CharField(max_length=100, choices = CHOICES)
    Contact = models.CharField(max_length=100, default='')


class Contact(models.Model):
    Name=models.CharField(max_length=150)
    Email=models.CharField(max_length=50)
    Subject=models.CharField(max_length=50)
    Message=models.CharField(max_length=400)
    def __str__(self):
        return self.Name
