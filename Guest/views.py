from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import *
from Hospital.models import *
from django.core.mail import send_mail
from django.conf import settings

import random
# Create your views here.

def home(request):
    return render(request,"Guest/Home.html")

def hospital(request):
    ho=Hospitaltype.objects.all()
    di=District.objects.all()
    if request.method=="POST":
        pl=Place.objects.get(id=request.POST.get('txtplace'))
        ht=Hospitaltype.objects.get(id=request.POST.get('txttype'))
        Hospital.objects.create(name=request.POST.get('txtname'),contact=request.POST.get('txtnumber'),email=request.POST.get('txtemail'),address=request.POST.get('txtaddress'),logo=request.FILES.get('txtlogo'),proof=request.FILES.get('txtproof'),place=pl,hospitaltype=ht,password=request.POST.get('txtpass'))
        
        send_mail(
            'Respected Sir/Madam '+request.POST.get('txtname'),#subject
            "\rYour Hospital registration is successful",#body
            settings.EMAIL_HOST_USER,
            [request.POST.get('txtemail')],
        )
        return render(request,"Guest/NewHospital.html",{'ho':ho,'di':di})
    else:
        return render(request,"Guest/NewHospital.html",{'ho':ho,'di':di})


def newuser(request):
    di=District.objects.all()
    if request.method=="POST":
        pl=Place.objects.get(id=request.POST.get('txtplace'))
        NewUser.objects.create(name=request.POST.get('txtname'),contact=request.POST.get('txtnumber'),email=request.POST.get('txtemail'),address=request.POST.get('txtaddress'),gender=request.POST.get('txtgender'),place=pl,photo=request.FILES.get('txtproof'),password=request.POST.get('txtpass'))
        
        send_mail(
            'Respected Sir/Madam '+request.POST.get('txtname'),#subject
            "\rYour registration is successful",#body
            settings.EMAIL_HOST_USER,
            [request.POST.get('txtemail')],
        )
        return render(request,"Guest/NewUser.html",{'di':di})
    else:
        return render(request,"Guest/NewUser.html",{'di':di})

def Ajaxpla(request):
    di=District.objects.get(id=request.GET.get('district'))
    pl=Place.objects.filter(district=di)
    return render(request,"Guest/AjaxPlace.html",{'pl':pl})


def Login(request):
    if request.method=="POST":
        hcount=Hospital.objects.filter(email=request.POST.get('txtemail'),password=request.POST.get('txtpassword'),status=1).count()
        ucount=NewUser.objects.filter(email=request.POST.get('txtemail'),password=request.POST.get('txtpassword')).count()
        ccount=Consultancy.objects.filter(email=request.POST.get('txtemail'),password=request.POST.get('txtpassword')).count()
        dcount=Doctor.objects.filter(email=request.POST.get('txtemail'),password=request.POST.get('txtpassword')).count()
        acount=Adminlogin.objects.filter(email=request.POST.get('txtemail'),password=request.POST.get('txtpassword')).count()
        if hcount>0:
            hos=Hospital.objects.get(email=request.POST.get('txtemail'),password=request.POST.get('txtpassword'),status=1)
            request.session["hid"]=hos.id
            request.session["hname"]=hos.name
            return redirect("hospital:Home")
        elif ucount>0:
            user=NewUser.objects.get(email=request.POST.get('txtemail'),password=request.POST.get('txtpassword'))
            request.session["uid"]=user.id
            request.session["uname"]=user.name
            request.session["email"]=user.email
            return redirect("user:Home")
        elif ccount>0:
            consultancy=Consultancy.objects.get(email=request.POST.get('txtemail'),password=request.POST.get('txtpassword'))
            request.session["cid"]=consultancy.id
            request.session["cname"]=consultancy.name
            request.session["hosid"]=consultancy.hospital_id_id
            return redirect("consultancy:Home")
        elif dcount>0:
            doc=Doctor.objects.get(email=request.POST.get('txtemail'),password=request.POST.get('txtpassword'))
            request.session["did"]=doc.id
            request.session["dname"]=doc.name
            return redirect("doctor:Home")
        elif acount>0:
            ad=Adminlogin.objects.get(email=request.POST.get('txtemail'),password=request.POST.get('txtpassword'))
            request.session["aid"]=ad.id
            request.session["aname"]=ad.name
            return redirect("webadmin:Home")
        else:
            pass

    return render(request,"Guest/Login.html")

def ForgetPassword(request):
    
    if request.method=="POST":
        otp=random.randint(10000, 999999)
        request.session["otp"]=otp
        request.session["femail"]=request.POST.get('txtemail')
        send_mail(
            'Respected Sir/Madam ',#subject
            "\rYour OTP for Reset Password Is"+str(otp),#body
            settings.EMAIL_HOST_USER,
            [request.POST.get('txtemail')],
        )
        return redirect("guest:verification")
    else:
        return render(request,"Guest/ForgetPassword.html")

def OtpVerification(request):
    if request.method=="POST":
        otp=int(request.session["otp"])
        if int(request.POST.get('txtotp'))==otp:
            return redirect("guest:create")
    return render(request,"Guest/OTPVerification.html")

def CreateNewPass(request):
    if request.method=="POST":
        if request.POST.get('txtpassword2')==request.POST.get('txtpassword3'):
            usercount=NewUser.objects.filter(email=request.session["femail"]).count()
            doctorcount=Doctor.objects.filter(email=request.session["femail"]).count()
            consultancycount=Consultancy.objects.filter(email=request.session["femail"]).count()
            hospitalcount=hospital.objects.filter(email=request.session["femail"]).count()
            if usercount>0:
                user=NewUser.objects.get(email=request.session["femail"])
                user.password=request.POST.get('txtpassword2')
                user.save()
                return redirect("guest:Logins")

            elif doctorcount>0:
                doc=Doctor.objects.get(email=request.session["femail"])
                doc.password=request.POST.get('txtpassword2')
                doc.save()
                return redirect("guest:Logins")

            elif consultancycount>0:
                con=Consultancy.objects.get(email=request.session["femail"])
                con.password=request.POST.get('txtpassword2')
                con.save()
                return redirect("guest:Logins")

            else:
                hos=Hospital.objects.get(email=request.session["femail"])
                hos.password=request.POST.get('txtpassword2')
                hos.save()
                return redirect("guest:Logins")
    else:       
        return render(request,"Guest/CreateNewPassword.html")