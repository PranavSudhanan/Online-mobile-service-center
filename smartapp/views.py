from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import *
from .forms import *
from smartproject.settings import EMAIL_HOST_USER

# Create your views here.


def index(request):
    return render(request, 'index.html')


def aboutus(request):
    return render(request, 'aboutus.html')

def indexcontact(request):
    if request.method == 'POST':
        a = contactform(request.POST)
        if a.is_valid():
            fn = a.cleaned_data['fname']
            em = a.cleaned_data['email']
            st = a.cleaned_data['subject']
            ms = a.cleaned_data['message']
            b = contactmodel(fname=fn, email=em, subject=st, message=ms)
            b.save()
            return render(request, 'reviewalert')
        else:
            return HttpResponse("Failed!")
    else:
        return render(request, 'indexcontact.html')


def contactus(request):
    return render(request, 'contactus.html')


def testimonials(request):
    return render(request, 'testimonials.html')


def centerregistration(request):
    if request.method=='POST':
        a = servicecenterform(request.POST)
        if a.is_valid():
            nm = a.cleaned_data['companyname']
            em = a.cleaned_data['email']
            ph = a.cleaned_data['number']
            ps = a.cleaned_data['password']
            cp = a.cleaned_data['cpassword']
            ad = a.cleaned_data['address']
            if ps==cp:
                b = servicecentermodel(companyname=nm, email=em, number=ph, password=ps, address=ad)
                b.save()
                # return HttpResponse("Registration Success....")
                return redirect(centerlogin)
            else:
                return HttpResponse("Incorrect Password!")
        else:
            return HttpResponse("Registration Failed!")
    else:
        return render(request,'centerregistration.html')


def centerlogin(request):
    if request.method == 'POST':
        a = serviceloginform(request.POST)
        if a.is_valid():
            em = a.cleaned_data['email']
            ps = a.cleaned_data['password']
            b = servicecentermodel.objects.all()
            for i in b:
                cmp = i.companyname
                request.session['companyname'] = cmp
                id = i.id
                if i.email == em and i.password == ps:
                    # return HttpResponse("Login Success")
                    return render(request, 'centerprofile.html',{'cmp':cmp, 'id':id})
            else:
                return HttpResponse("Login failed")
    else:
        return render(request, 'centerlogin.html')

def centeredit(request, id):
    a = servicecentermodel.objects.get(id=id)
    if request.method == 'POST':
        a.companyname = request.POST.get("companyname")
        a.email = request.POST.get("email")
        a.number = request.POST.get("number")
        a.password = request.POST.get("password")
        a.address = request.POST.get("address")
        a.save()
        return redirect(centerlogin)
    return render(request, 'editcenter.html', {'a': a})

def centerdelete(request, id):
    a = servicecentermodel.objects.get(id=id)
    a.delete()
    return HttpResponse("Account Deleted Successfully")


def servicecenterprofile(request):
    return render(request, 'centerprofile.html')


def addmobiles(request):
    if request.method == 'POST':
        a = addmobileform(request.POST, request.FILES)
        if a.is_valid():
            ig = a.cleaned_data['image']
            nm = a.cleaned_data['mname']
            tp = a.cleaned_data['type']
            b = addmobilemodel(image=ig, mname=nm, type=tp)
            b.save()
            # return HttpResponse("Product Uploaded Successfully...")
            return redirect(mobiletype)
        else:
            return HttpResponse("Product Upload failed!")
    return render(request, 'addmobiles.html')


def mobiletype(request):
    return render(request, 'mobiletype.html')


def mobiledisplay(request):
    a = addmobilemodel.objects.all()
    im = []
    mname = []
    type = []
    id = []
    for i in a:
        id1 = i.id
        id.append(id1)
        img = i.image
        im.append(str(img).split('/')[-1])
        nm = i.mname
        tp = i.type
        mname.append(nm)
        type.append(tp)
    mylist = zip(im, mname, type, id)
    return render(request, 'mobiledisplay.html', {'list': mylist})


def androiddisplay(request):
    a = addmobilemodel.objects.all()
    im = []
    mname = []
    type = []
    id = []
    for i in a:
        id1 = i.id
        id.append(id1)
        img = i.image
        im.append(str(img).split('/')[-1])
        nm = i.mname
        tp = i.type
        mname.append(nm)
        type.append(tp)
    mylist = zip(im, mname, type, id)
    return render(request, 'androiddisplay.html', {'list': mylist})


def addparts(request):
    if request.method == 'POST':
        a = addpartsform(request.POST, request.FILES)
        if a.is_valid():
            ig = a.cleaned_data['image']
            nm = a.cleaned_data['pname']
            pr = a.cleaned_data['price']
            tp = a.cleaned_data['type']
            b = partsmodel(image=ig, pname=nm, price=pr, type=tp)
            b.save()
            # return HttpResponse("Product Uploaded Successfully...")
            return redirect(partsdisplay)
        else:
            return HttpResponse("Product Upload failed!")
    return render(request, 'addparts.html')


def partsdisplay(request):
    a = partsmodel.objects.all()
    im = []
    pname = []
    price = []
    type = []
    id = []
    for i in a:
        id1 = i.id
        id.append(id1)
        img = i.image
        im.append(str(img).split('/')[-1])
        nm = i.pname
        pr = i.price
        tp = i.type
        pname.append(nm)
        price.append(pr)
        type.append(tp)
    mylist = zip(im, pname, price, type, id)
    return render(request, 'partsdisplay.html', {'list': mylist})


def androidparts(request):
    a = partsmodel.objects.all()
    im = []
    pname = []
    price = []
    type = []
    id = []
    for i in a:
        id1 = i.id
        id.append(id1)
        img = i.image
        im.append(str(img).split('/')[-1])
        nm = i.pname
        pr = i.price
        tp = i.type
        pname.append(nm)
        price.append(pr)
        type.append(tp)
    mylist = zip(im, pname, price, type, id)
    return render(request, 'androidparts.html', {'list': mylist})


def userregistration(request):
    if request.method=='POST':
           un=request.POST.get("username")
           em=request.POST.get("email")
           ps=request.POST.get("password")
           cps=request.POST.get("cpassword")
           if ps==cps:
                b = User(username=un, email=em, password=ps)
                b.save()
                return redirect(userlogin)
           else:
               return HttpResponse("Registration Failed!")
    else:
        return render(request,'userregistration.html')


def userlogin(request):
    if request.method == 'POST':
        a = userlogform(request.POST)
        if a.is_valid():
            em = a.cleaned_data['email']
            ps = a.cleaned_data['password']
            b = User.objects.all()
            for i in b:
                usr = i.username
                if i.email == em and i.password == ps:
                    id = i.id
                    request.session['id'] = i.id
                    return render(request, "userprofile.html", {'usr':usr, 'id':id})
            else:
                return HttpResponse("Login failed")
    else:
        return render(request, 'userlogin.html')


def useredit(request, id):
    a = User.objects.get(id=id)
    if request.method == 'POST':
        a.username = request.POST.get("username")
        a.email = request.POST.get("email")
        a.password = request.POST.get("password")
        a.save()
        return redirect(userlogin)
    return render(request, 'edituser.html', {'a': a})


def userdelete(request, id):
    a = User.objects.get(id=id)
    a.delete()
    return HttpResponse("Account Deleted Successfully")


def userprofile(request):
    return render(request, 'userprofile.html')


def repairregister(request):
    if request.method=='POST':
        a = repairform(request.POST)
        if a.is_valid():
            pn = a.cleaned_data['phone']
            cm = a.cleaned_data['complaint']
            wy = a.cleaned_data['warranty']
            fn = a.cleaned_data['fname']
            nm = a.cleaned_data['number']
            em = a.cleaned_data['email']
            ad = a.cleaned_data['address']
            b = repairmodel(phone=pn, complaint=cm, warranty=wy, fname=fn, number=nm, email=em, address=ad)
            b.save()
            subject = f"Repair Booked for {pn}"
            message = f"hello {fn}\n your repair order for {pn} {cm} is placed successfully. Our delivery executive will pickup your device within next 2 working days.\n\n We will return your product after resolving the issue, it could take upto 10 working days. We will inform you once the service is completed.\n\n Order Details:\n Product Name: {pn}\n MRP: {pr}\n Customer Details:\n Name: {fn}\n Address: {ad}\n Number: {nm}\n Payment Mode: {pm}"
            email_from = EMAIL_HOST_USER
            send_mail(subject, message, email_from, [em])
            return HttpResponse("Registration Success....")
        else:
            return HttpResponse("Registration Failed!")
    else:
        return render(request,'repairregister.html')


def newbookings(request):
    a = repairmodel.objects.all()
    return render(request, 'newbookings.html', {'a':a})


def deletebooking(request, id):
    a = repairmodel.objects.get(id=id)
    a.delete()
    return redirect(newbookings)


def repairinfo(request, id):
    b = repairmodel.objects.get(id=id)
    pnn = b.phone
    cmt = b.complaint
    wty = b.warranty
    fne = b.fname
    num = b.number
    eml = b.email
    add = b.address
    if request.method=='POST':
        a = repairinfoform(request.POST)
        if a.is_valid():
            pn = a.cleaned_data['phone']
            cm = a.cleaned_data['complaint']
            wy = a.cleaned_data['warranty']
            ss = a.cleaned_data['status']
            fn = a.cleaned_data['fname']
            nm = a.cleaned_data['number']
            em = a.cleaned_data['email']
            ad = a.cleaned_data['address']
            b = repairinfomodel(phone=pn, complaint=cm, warranty=wy, status=ss, fname=fn, number=nm, email=em, address=ad)
            b.save()
            return redirect(repairinfodisplay)
        else:
            return HttpResponse("Registration Failed!")
    else:
        return render(request,'repairstatus.html', {'pnn':pnn, 'cmt':cmt, 'wty':wty, 'fne':fne, 'num':num, 'eml':eml, 'add':add})


def repairinfodisplay(request):
    a = repairinfomodel.objects.all()
    return render(request, 'repairinfodisplay.html', {'a': a})


def repairinfouser(request):
    a = repairinfomodel.objects.all()
    b = request.session['id']
    return render(request, 'repairinfouser.html', {'a':a, 'b':b})


def servicecomplete(request, id):
    b = repairmodel.objects.get(id=id)
    pn = b.phone
    cm = b.complaint
    fn = b.fname
    nm = b.number
    em = b.email
    ad = b.address
    a = repairinfomodel.objects.get(id=id)
    if request.method == 'POST':
        a.phone = request.POST.get("phone")
        a.complaint = request.POST.get("complaint")
        a.warranty = request.POST.get("warranty")
        a.status = request.POST.get("status")
        a.cost = request.POST.get("cost")
        a.fname = request.POST.get("fname")
        a.number = request.POST.get("number")
        a.email = request.POST.get("email")
        a.address = request.POST.get("address")
        a.save()
        ct = a.cost
        subject = f"Service Completed for {pn}"
        message = f"hello {fn}\n your repair order for {pn} {cm} is Completed. Our delivery executive will return your device within the next 5 working days\n\n Order Details:\n Product Name: {pn}\n Repair Cost: {ct}\n Customer Details:\n Name: {fn}\n Address: {ad}\n Number: {nm}\n"
        email_from = EMAIL_HOST_USER
        send_mail(subject, message, email_from, [em])
        return redirect(servicecompletedisplay)
    return render(request, 'repairstatusedit.html', {'a': a})


def servicecompletedisplay(request):
    a = repairinfomodel.objects.all()
    return render(request, 'servicecompleted.html', {'a':a})


def buyparts(request, id):
    b = partsmodel.objects.get(id=id)
    pnn = b.pname
    prc = b.price
    c = addmobilemodel.objects.get(id=id)
    mnm = c.mname
    if request.method == 'POST':
        a = buypartsform(request.POST)
        if a.is_valid():
            pn = a.cleaned_data['pname']
            pr = a.cleaned_data['price']
            md = a.cleaned_data['model']
            fn = a.cleaned_data['fname']
            nm = a.cleaned_data['number']
            em = a.cleaned_data['email']
            ad = a.cleaned_data['address']
            pm = a.cleaned_data['paymode']
            b = buypartsmodel(pname=pn, price=pr, model=md, fname=fn, number=nm, email=em, address=ad, paymode=pm)
            b.save()
            subject = f"Order Placed {pn} for {mnm}"
            message = f"hello {fn}\n your order for {mnm} {pn} is placed successfully. Expect delivery within next 5 working days\n\n Order Details:\n Product Name: {pn}\n MRP: {pr}\n Customer Details:\n Name: {fn}\n Address: {ad}\n Number: {nm}\n Payment Mode: {pm}"
            email_from = EMAIL_HOST_USER
            send_mail(subject, message, email_from, [em])
            return render(request, 'partsordersuccess.html')
            # return HttpResponse("Sale Success")
        else:
            return HttpResponse("Failed!")
    else:
        return render(request,'buyparts.html', {'pnn':pnn, 'prc':prc, 'mnm':mnm})


def recycle(request):
    if request.method == 'POST':
        a = recycleform(request.POST)
        if a.is_valid():
            dn = a.cleaned_data['dname']
            yr = a.cleaned_data['year']
            md = a.cleaned_data['model']
            fn = a.cleaned_data['fname']
            nm = a.cleaned_data['number']
            em = a.cleaned_data['email']
            ad = a.cleaned_data['address']
            b = recyclemodel(dname=dn, year=yr, model=md, fname=fn, number=nm, email=em, address=ad)
            b.save()
            subject = f"Thank you for staying green"
            message = f"hello {fn}\n You chose the right path in recycling your obsolete device. Your contribution plays a major role in reducing e-waste. Our delivery agent will pick up your device within the next 3 working days\n Team R.Smart\n\n Item Details:\n Product Name: {dn}\n Year: {yr}\n Customer Details:\n Name: {fn}\n Address: {ad}\n Number: {nm}"
            email_from = EMAIL_HOST_USER
            send_mail(subject, message, email_from, [em])
            return render(request, 'recyclesuccess.html')
        else:
            return HttpResponse("Failed!")
    else:
        return render(request,'recycle.html')


def writereview(request, id):
    b = User.objects.get(id=id)
    un = b.username
    el = b.email
    if request.method == 'POST':
        a = writereviewform(request.POST)
        if a.is_valid():
            fn = a.cleaned_data['fname']
            em = a.cleaned_data['email']
            st = a.cleaned_data['subject']
            ms = a.cleaned_data['message']
            b = writereviewmodel(fname=fn, email=em, subject=st, message=ms)
            b.save()
            return HttpResponse("Submitted!")
        else:
            return HttpResponse("Failed!")
    else:
        return render(request, 'writereview.html', {'un':un, 'el':el})


def viewreview(request, id):
    a = writereviewmodel.objects.all()
    b = servicecentermodel.objects.get(id=id)
    cn = b.companyname
    return render(request, 'viewreview.html', {'a':a, 'cn':cn})


def writecomplaint(request, id):
    b = User.objects.get(id=id)
    un = b.username
    el = b.email
    if request.method == 'POST':
        a = writecomplaintform(request.POST)
        if a.is_valid():
            fn = a.cleaned_data['fname']
            em = a.cleaned_data['email']
            cm = a.cleaned_data['company']
            st = a.cleaned_data['subject']
            ms = a.cleaned_data['message']
            b = writecomplaintmodel(fname=fn, email=em, company=cm, subject=st, message=ms)
            b.save()
            return render(request, 'reviewalert')
        else:
            return HttpResponse("Failed!")
    else:
        return render(request, 'writecomplaint.html', {'un': un, 'el': el})


def viewcomplaint(request, id):
    a = writecomplaintmodel.objects.all()
    b = servicecentermodel.objects.get(id=id)
    cn = b.companyname
    return render(request, 'viewcomplaint.html', {'a':a, 'cn':cn})


def complaintreview(request, id):
    a = writecomplaintmodel.objects.get(id=id)
    fn = a.fname
    em = a.email
    cm = a.company
    subject = f"{cm}"
    message = f"hello {fn}\n We are extremely sorry for the inconvinience, Our staffs are highly experienced and this kindof issues have not been reported before. We can arrange a free service for you. Just place a new repair request and we will resolve your issue free of cost\n Team R.Smart"
    email_from = EMAIL_HOST_USER
    send_mail(subject, message, email_from, [em])
    return render(request, 'complaintalert')


def contactwrite(request):
    if request.method == 'POST':
        a = contactform(request.POST)
        if a.is_valid():
            fn = a.cleaned_data['fname']
            em = a.cleaned_data['email']
            st = a.cleaned_data['subject']
            ms = a.cleaned_data['message']
            b = contactmodel(fname=fn, email=em, subject=st, message=ms)
            b.save()
            return render(request, 'reviewalert.html')
        else:
            return HttpResponse("Failed!")
    else:
        return render(request, 'contactus.html')


def displaytestimony(request):
    a = contactmodel.objects.all()
    return render(request, 'testimonials.html', {'a':a})


def storesoffline(request):
    return render(request, 'offlinestores.html')




