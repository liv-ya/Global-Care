from django.shortcuts import render,redirect
from Hospital.models import Doctor
from User.models import Appointment
from Doctor.models import MedicineReport,Prescribtion
from Guest.models import NewUser
from Admin.models import Complainttype,complaint,feedback
# Create your views here.
def HomePage(request):
    if 'did' in request.session:
        do=Doctor.objects.get(id=request.session["did"])
        return render(request,"Doctor/HomePage.html",{'data':do})
    else:
        return redirect("guest:Logins")

def MyProfile(request):
    if 'did' in request.session:
        con=Doctor.objects.get(id=request.session["did"])
        return render(request,"Doctor/MyProfile.html",{'con':con})
    else:
        return redirect("guest:Logins")

def EditProfile(request):
    if 'did' in request.session:
        us=Doctor.objects.get(id=request.session["did"])
        if request.method=="POST":
            us.name=request.POST.get('txtname')
            us.contact=request.POST.get('txtnumber')
            us.address=request.POST.get('txtaddress')
            us.save()
            return redirect("doctor:Profile")
        else:
            return render(request,"Doctor/EditProfile.html",{'us':us})
    else:
        return redirect("guest:Logins")

def ChangePassword(request):
    if 'did' in request.session:
        if request.method=="POST":
            ccount=Doctor.objects.filter(id=request.session["did"],password=request.POST.get('txtpassword1')).count()
            if ccount>0:
                doc=Doctor.objects.get(id=request.session["did"],password=request.POST.get('txtpassword1'))
                doc.password=request.POST.get('txtpassword2')
                doc.save()
                return redirect("doctor:Home")
            else:
                return redirect("doctor:CPass")
        else:   
            return render(request,"Doctor/ChangePassword.html")
    else:
        return redirect("guest:Logins")

def UserAppointments(request):
    if 'did' in request.session:
        doc=Doctor.objects.get(id=request.session["did"])
        appoint=Appointment.objects.filter(slot__davaillable__doctor=doc,appointment_status=1)
        return render(request,"Doctor/ViewAppointment.html",{'data':appoint})
    else:
        return redirect("guest:Logins")

def UserConsulted(request,aid):
    if 'did' in request.session:
        ac=Appointment.objects.get(id=aid)
        ac.appointment_status=3
        ac.save()
        return redirect("doctor:Viewappoint")
    else:
        return redirect("guest:Logins")
        

def ViewConsulted(request):
    if 'did' in request.session:
        doc=Doctor.objects.get(id=request.session["did"])
        appoint=Appointment.objects.filter(slot__davaillable__doctor=doc,appointment_status=3)
        return render(request,"Doctor/ViewConsulted.html",{'data':appoint})
    else:
        return redirect("guest:Logins")
        

def UpMediReport(request,mid):
    if 'did' in request.session:
        do=Doctor.objects.all()
        if request.method=="POST":
            app=Appointment.objects.get(id=mid)
            MedicineReport.objects.create(report_file=request.POST.get('txtfile'),report_details=request.POST.get('txtreport'),major=request.POST.get('txtmajor'),appointment=app)
            return render(request,"Doctor/UpdateReport.html",{'app':do})
        else:
            return render(request,"Doctor/UpdateReport.html",{'app':do})
    else:
        return redirect("guest:Logins")

def AddPrescribtion(request,pid):
    if 'did' in request.session:
        do=Doctor.objects.all()
        if request.method=="POST":
            app=Appointment.objects.get(id=pid)
            Prescribtion.objects.create(medicine_details=request.POST.get('txtmedi'),diet=request.POST.get('txtdiet'),appointment=app)
            return render(request,"Doctor/Prescribtion.html",{'app':do})
        else:
            return render(request,"Doctor/Prescribtion.html",{'app':do})
    else:
        return redirect("guest:Logins")

def ViewHistory(request,hid):
    if 'did' in request.session:
        appoint=Appointment.objects.get(id=hid)
        userid=appoint.user.id
        user=NewUser.objects.get(id=userid)
        medireport=MedicineReport.objects.filter(appointment__user=user)
        preport=Prescribtion.objects.filter(appointment__user=user)
        return render(request,"Doctor/ViewHistory.html",{'med':medireport,'pr':preport})
    else:
        return redirect("guest:Logins")

def Sendcomplaint(request):
    if 'did' in request.session:
        nu=int(request.session["did"])
        ctype=Complainttype.objects.all()
        dt=complaint.objects.filter(doctor=nu)
        if request.method=="POST":
            com=Complainttype.objects.get(id=request.POST.get('complaint_type'))
            complaint.objects.create(typeid=com,title=request.POST.get('txttit'),content=request.POST.get('txtcont'),doctor=nu)
            return render(request,"Doctor/Complaint.html",{'data':dt,'complaint_type':ctype})
        else:
            return render(request,"Doctor/Complaint.html",{'data':dt,'complaint_type':ctype})
    else:
        return redirect("guest:Logins")

def DelComplaint(request,cid):
    if 'did' in request.session:
        com=complaint.objects.get(id=cid)
        com.delete()
        return redirect("doctor:Home")
    else:
        return redirect("guest:Logins")
    

def SendFeedBack(request):
    if 'did' in request.session:
        nu=int(request.session["did"])
        dt=feedback.objects.filter(doctor=nu)
        if request.method=="POST":
            feedback.objects.create(content=request.POST.get('txtmedi'),doctor=nu)
            return render(request,"Doctor/Feedback.html",{'dt':dt})
        else:
            return render(request,"Doctor/Feedback.html",{'dt':dt})
    else:
        return redirect("guest:Logins")

def DelFeedback(request,cid):
    if 'did' in request.session:
        com=feedback.objects.get(id=cid)
        com.delete()
        return redirect("doctor:Home")
    else:
        return redirect("guest:Logins")

def logout(request):
    del request.session["did"]
    return redirect("guest:Logins")