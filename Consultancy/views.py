from django.shortcuts import render,redirect
from Hospital.models import Consultancy,Doctor
from Guest.models import Hospital,NewUser
from Consultancy.models import *
from User.models import Appointment
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def HomePage(request):
    if 'cid' in request.session:
        ad=Consultancy.objects.get(id=request.session["cid"])
        return render(request,"Consultancy/HomePage.html",{'data':ad})
    else:
        return redirect("guest:Logins")

def MyProfile(request):
    if 'cid' in request.session:
        con=Consultancy.objects.get(id=request.session["cid"])
        return render(request,"Consultancy/MyProfile.html",{'con':con})
    else:
        return redirect("guest:Logins")


def EditProfile(request):
    if 'cid' in request.session:
        co=Consultancy.objects.get(id=request.session["cid"])
        if request.method=="POST":
            co.name=request.POST.get('txtname')
            co.headname=request.POST.get('txtheadname')
            co.save()
            return redirect("consultancy:Profile")
        else:
            return render(request,"Consultancy/EditProfile.html",{'co':co})
    else:
        return redirect("guest:Logins")

def ChangePassword(request):
    if 'cid' in request.session:
        if request.method=="POST":
            ccount=Consultancy.objects.filter(id=request.session["cid"],password=request.POST.get('txtpassword1')).count()
            if ccount>0:
                consultancy=Consultancy.objects.get(id=request.session["cid"],password=request.POST.get('txtpassword1'))
                consultancy.password=request.POST.get('txtpassword2')
                consultancy.save()
                return redirect("consultancy:Home")
            else:
                return redirect("consultancy:CPass")
        else:   
            return render(request,"Consultancy/ChangePassword.html")
    else:
        return redirect("guest:Logins")

def ViewDoctors(request):
    if 'cid' in request.session:
        hos=Hospital.objects.get(id=request.session["hosid"])
        dc=Doctor.objects.filter(hospital=hos)
        return render(request,"Consultancy/ViewDoctors.html",{'data':dc})
    else:
        return redirect("guest:Logins")

def SetAvailability(request,did):
    if 'cid' in request.session:
        doc=Doctor.objects.get(id=did)
        av=availability.objects.filter(doctor=doc)
        if request.method=="POST":
            availability.objects.create(doctor=doc,date=request.POST.get('txtdate'),from_time=request.POST.get('txtftime'),To_time=request.POST.get('txtttime'))
            return render(request,"Consultancy/Availability.html",{'res':av})
        else:
            return render(request,"Consultancy/Availability.html",{'res':av})
    else:
        return redirect("guest:Logins")

def gentoken(request,did):
    if 'cid' in request.session:
        av=availability.objects.get(id=did)
        if request.method=="POST":
            tokencount=int(request.POST.get('txttoken'))
            for i in range(1,tokencount+1):
                Slots.objects.create(slotno=i,davaillable=av)
            return redirect("consultancy:VD")
        else:
            return render(request,"Consultancy/GenerateToken.html")
    else:
        return redirect("guest:Logins")

def UserAppointment(request):
    if 'cid' in request.session:
        hos=Hospital.objects.get(id=request.session["hosid"])
        appoint=Appointment.objects.filter(slot__davaillable__doctor__hospital=hos,appointment_status=0)
        return render(request,"Consultancy/NewUserAppointment.html",{'data':appoint})
    else:
        return redirect("guest:Logins")

def AcceptAppointment(request):
    if 'cid' in request.session:
        hos=Hospital.objects.get(id=request.session["hosid"])
        appoint=Appointment.objects.filter(slot__davaillable__doctor__hospital=hos,appointment_status=1)
        return render(request,"Consultancy/AcceptedAppointment.html",{'data':appoint})
    else:
        return redirect("guest:Logins")

def RejectAppointment(request):
    if 'cid' in request.session:
        hos=Hospital.objects.get(id=request.session["hosid"])
        appoint=Appointment.objects.filter(slot__davaillable__doctor__hospital=hos,appointment_status=2)
        return render(request,"Consultancy/RejectedAppointment.html",{'data':appoint})
    else:
        return redirect("guest:Logins")

def AcceptedAppointement(request,aid):
    if 'cid' in request.session:
        ac=Appointment.objects.get(id=aid)
        ac.appointment_status=1
        ac.save()
        return redirect("consultancy:Viewappoint")
    else:
        return redirect("guest:Logins")


def RejectededAppointement(request,rid):
    if 'cid' in request.session:
        rej=Appointment.objects.get(id=rid)
        rej.appointment_status=2
        rej.save()
        return redirect("consultancy:Viewappoint")
    else:
        return redirect("guest:Logins")

   
def logout(request):
    del request.session["cid"]
    return redirect("guest:Logins")

    
def AppointmentCancel(request,aid):
    ap=Appointment.objects.get(id=aid)
    users=ap.user_id
    user=NewUser.objects.get(id=users)
    if request.method=="POST":
        send_mail(
            'Respected Sir/Madam ',#subject
            request.POST.get('txtmedi'),#body
            settings.EMAIL_HOST_USER,
            [user.email],
        )
        return render(request,"Consultancy/AppointmentCancel.html")
    else:        
        return render(request,"Consultancy/AppointmentCancel.html")



