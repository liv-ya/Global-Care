from django.shortcuts import render,redirect
from Guest.models import NewUser
from Admin.models import *
from Guest.models import Hospital
from Hospital.models import Doctor
from Consultancy.models import availability,Slots
from User.models import Appointment
from Doctor.models import Prescribtion,MedicineReport
# Create your views here.
def HomePage(request):
    if 'uid' in request.session:
        ad=NewUser.objects.get(id=request.session["uid"])
        return render(request,"User/HomePage.html",{'data':ad})
    else:
        return redirect("guest:Logins")


def MyProfile(request):
    if 'uid' in request.session:
        us=NewUser.objects.get(id=request.session["uid"])
        return render(request,"User/MyProfile.html",{'us':us})
    else:
        return redirect("guest:Logins")


def EditProfile(request):
    if 'uid' in request.session:
        us=NewUser.objects.get(id=request.session["uid"])
        if request.method=="POST":
            us.name=request.POST.get('txtname')
            us.contact=request.POST.get('txtnumber')
            us.address=request.POST.get('txtaddress')
            us.save()
            return redirect("user:Profile")
        else:
            return render(request,"User/EditProfile.html",{'us':us})
    else:
        return redirect("guest:Logins")

def ChangePassword(request):
    if 'uid' in request.session:
        if request.method=="POST":
            uscount=NewUser.objects.filter(id=request.session["uid"],password=request.POST.get('txtpassword1')).count()
            if uscount>0:
                users=NewUser.objects.get(id=request.session["uid"],password=request.POST.get('txtpassword1'))
                users.password=request.POST.get('txtpassword2')
                users.save()
                return redirect("user:Home")
            else:
                return redirect("user:CPass")
        else:   
            return render(request,"User/ChangePassword.html")
    else:
        return redirect("guest:Logins")


def SearchHospital(request):
    if 'uid' in request.session:
        di=District.objects.all()
        ho=Hospital.objects.filter(status=1)
        return render(request,"User/SearchHospital.html",{'di':di,'ho':ho})
    else:
        return redirect("guest:Logins")


def ViewDoctor(request,hid):
    if 'uid' in request.session:
        hos=Hospital.objects.get(id=hid)
        request.session["vdid"]=hid
        dep=Department.objects.all()
        doc=Doctor.objects.filter(hospital=hos)
        return render(request,"User/ViewDoctors.html",{'dep':dep,'doc':doc})
    else:
        return redirect("guest:Logins")

def ViewAvailability(request,did):
    if 'uid' in request.session:
        doc=Doctor.objects.get(id=did)
        av=availability.objects.filter(doctor=doc)
        return render(request,"User/ViewAvailability.html",{'res':av})
    else:
        return redirect("guest:Logins")

def ViewSlot(request,did):
    if 'uid' in request.session:
        av=availability.objects.get(id=did)
        COUNTS=Slots.objects.filter(davaillable=av,status=0).count()
        if COUNTS>0:

            sl=Slots.objects.filter(davaillable=av,status=0)[0]
            return render(request,"User/ViewSlot.html",{'data':sl})
        else:
            return render(request,"User/ViewSlot.html")
    else:
        return redirect("guest:Logins")

def AjaxHos(request):
    if request.GET.get('place')!="":
        pid=Place.objects.get(id=request.GET.get('place'))
        hos=Hospital.objects.filter(place=pid,status=1)
        return render(request,"User/AjaxHospital.html",{'data':hos})
    else:
        did=District.objects.get(id=request.GET.get('district'))
        hos=Hospital.objects.filter(place__district=did,status=1)
        return render(request,"User/AjaxHospital.html",{'data':hos})

def AjaxDoc(request):
    hos=Hospital.objects.get(id=request.session["vdid"])
    dept=Department.objects.get(id=request.GET.get('dept'))
    doc=Doctor.objects.filter(hospital=hos,department=dept)
    return render(request,"User/AjaxDoc.html",{'data':doc})

def ConfirmAppointment(request,sid):
    if 'uid' in request.session:
        sl=Slots.objects.get(id=sid)
        request.session["cfid"]=sid
        if request.method=="POST":
            adate=sl.davaillable.date
            userid=NewUser.objects.get(id=request.session["uid"])
            Appointment.objects.create(slot=sl,appointment_date=adate,user=userid)
            sl.status=1
            sl.save()
            return redirect("user:PrintAppointment")
        else:
            return render(request,"User/ConfirmAppointment.html",{'sl':sl})
    else:
        return redirect("guest:Logins")

def UserAppointment(request):
    if 'uid' in request.session:
        userid=NewUser.objects.get(id=request.session["uid"])
        appoint=Appointment.objects.filter(user=userid)
        return render(request,"User/ViewMyAppointments.html",{'data':appoint})
    else:
        return redirect("guest:Logins")

def ViewPrescrib(request,pid):
    if 'uid' in request.session:
        appoint=Appointment.objects.get(id=pid)
        pr=Prescribtion.objects.get(appointment=appoint)
        return render(request,"User/ViewPrescribtion.html",{'data':pr})
    else:
        return redirect("guest:Logins")


def Sendcomplaint(request):
    if 'uid' in request.session:
        nu=int(request.session["uid"])
        ctype=Complainttype.objects.all()
        dt=complaint.objects.filter(user=nu)
        if request.method=="POST":
            com=Complainttype.objects.get(id=request.POST.get('complaint_type'))
            complaint.objects.create(typeid=com,title=request.POST.get('txttit'),content=request.POST.get('txtcont'),user=nu)
            return render(request,"User/Complaint.html",{'data':dt,'complaint_type':ctype})
        else:
            return render(request,"User/Complaint.html",{'data':dt,'complaint_type':ctype})
    else:
        return redirect("guest:Logins")

def DelComplaint(request,cid):
    if 'uid' in request.session:
        com=complaint.objects.get(id=cid)
        com.delete()
        return redirect("user:Home")
    else:
        return redirect("guest:Logins")
    

def SendFeedBack(request):
    if 'uid' in request.session:
        nu=int(request.session["uid"])
        dt=feedback.objects.filter(user=nu)
        if request.method=="POST":
            feedback.objects.create(content=request.POST.get('txtmedi'),user=nu)
            return render(request,"User/Feedback.html",{'dt':dt})
        else:
            return render(request,"User/Feedback.html",{'dt':dt})
    else:
        return redirect("guest:Logins")
    

def DelFeedback(request,cid):
    if 'uid' in request.session:
        com=feedback.objects.get(id=cid)
        com.delete()
        return redirect("user:Home")
    else:
        return redirect("guest:Logins")

def ViewMedical(request,mid):
    if 'uid' in request.session:
        appoint=Appointment.objects.get(id=mid)
        mr=MedicineReport.objects.filter(appointment=appoint)
        return render(request,"User/ViewMedicineReport.html",{'data':mr})
    else:
        return redirect("guest:Logins")

def PrintApp(request):
    if 'uid' in request.session:
        sl=Slots.objects.get(id=request.session["cfid"])
        return render(request,"User/Print.html",{'sl':sl})
    else:
        return redirect("guest:Logins")

def logout(request):
    del request.session["uid"]
    return redirect("guest:Logins")