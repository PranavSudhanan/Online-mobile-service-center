from django import forms
from django.contrib.auth.models import User


class userregform(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class userlogform(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=20)

class servicecenterform(forms.Form):
    companyname = forms.CharField(max_length=25)
    email = forms.EmailField()
    password = forms.CharField(max_length=20)
    cpassword = forms.CharField(max_length=20)
    number = forms.IntegerField()
    address = forms.CharField(max_length=100)

class serviceloginform(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=20)

class addmobileform(forms.Form):
    image = forms.FileField()
    mname = forms.CharField(max_length=25)
    type = forms.CharField(max_length=40)

class addpartsform(forms.Form):
    image = forms.FileField()
    pname = forms.CharField(max_length=25)
    price = forms.CharField(max_length=40)
    type = forms.CharField(max_length=40)

class repairform(forms.Form):
    phone = forms.CharField(max_length=70)
    complaint = forms.CharField(max_length=150)
    warranty = forms.CharField(max_length=40)
    fname = forms.CharField(max_length=70)
    number = forms.IntegerField()
    email = forms.EmailField()
    address = forms.CharField(max_length=150)

class repairinfoform(forms.Form):
    phone = forms.CharField(max_length=70)
    complaint = forms.CharField(max_length=150)
    warranty = forms.CharField(max_length=40)
    status = forms.CharField(max_length=30)
    cost = forms.CharField(max_length=30)
    fname = forms.CharField(max_length=70)
    number = forms.IntegerField()
    email = forms.EmailField()
    address = forms.CharField(max_length=150)

class buypartsform(forms.Form):
    pname = forms.CharField(max_length=25)
    price = forms.CharField(max_length=40)
    model = forms.CharField(max_length=70)
    fname = forms.CharField(max_length=70)
    number = forms.IntegerField()
    email = forms.EmailField()
    address = forms.CharField(max_length=150)
    paymode = forms.CharField(max_length=50)

class recycleform(forms.Form):
    dname = forms.CharField(max_length=45)
    year = forms.IntegerField()
    model = forms.CharField(max_length=70)
    fname = forms.CharField(max_length=70)
    number = forms.IntegerField()
    email = forms.EmailField()
    address = forms.CharField(max_length=150)

class writereviewform(forms.Form):
    fname = forms.CharField(max_length=45)
    email = forms.EmailField()
    subject = forms.CharField(max_length=50)
    message = forms.CharField(max_length=150)

class writecomplaintform(forms.Form):
    fname = forms.CharField(max_length=45)
    email = forms.EmailField()
    company = forms.CharField(max_length=50)
    subject = forms.CharField(max_length=50)
    message = forms.CharField(max_length=150)

class contactform(forms.Form):
    fname = forms.CharField(max_length=45)
    email = forms.EmailField()
    subject = forms.CharField(max_length=50)
    message = forms.CharField(max_length=150)
