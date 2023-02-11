from django.db import models

# Create your models here.

class servicecentermodel(models.Model):
    companyname = models.CharField(max_length=25)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    number = models.IntegerField()
    address = models.CharField(max_length=100)

class addmobilemodel(models.Model):
    image = models.ImageField(upload_to='smartapp/static')
    mname = models.CharField(max_length=25)
    type = models.CharField(max_length=40)

class partsmodel(models.Model):
    image = models.ImageField(upload_to='smartapp/static')
    pname = models.CharField(max_length=25)
    price = models.CharField(max_length=40)
    type = models.CharField(max_length=40)

class repairmodel(models.Model):
    phone = models.CharField(max_length=70)
    complaint = models.CharField(max_length=150)
    warranty = models.CharField(max_length=40)
    fname = models.CharField(max_length=70)
    number = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=150)

class repairinfomodel(models.Model):
    choice = [
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed'),
        ('Out for delivery', 'Out for delivery'),
    ]

    phone = models.CharField(max_length=70)
    complaint = models.CharField(max_length=150)
    warranty = models.CharField(max_length=40)
    status = models.CharField(max_length=30, choices=choice)
    cost = models.CharField(max_length=30)
    fname = models.CharField(max_length=70)
    number = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=150)

class buypartsmodel(models.Model):
    choice = [
        ('Debit/Credit Card', 'Debit/Credit Card'),
        ('Upi', 'Upi'),
        ('Cash on delivery', 'Cash on delivery'),
    ]

    pname = models.CharField(max_length=25)
    price = models.CharField(max_length=40)
    model = models.CharField(max_length=70)
    fname = models.CharField(max_length=70)
    number = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=150)
    paymode = models.CharField(max_length=50, choices=choice)

class recyclemodel(models.Model):
    dname = models.CharField(max_length=45)
    year = models.IntegerField()
    model = models.CharField(max_length=70)
    fname = models.CharField(max_length=70)
    number = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=150)

class writereviewmodel(models.Model):
    fname = models.CharField(max_length=45)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=500)

class writecomplaintmodel(models.Model):
    fname = models.CharField(max_length=45)
    email = models.EmailField()
    company = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=500)

class contactmodel(models.Model):
    fname = models.CharField(max_length=45)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=500)

