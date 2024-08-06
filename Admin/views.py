from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
# Create your views here.
def department(request):
    if 'aid' in request.session:
        dep=Department.objects.all()
        if request.method=="POST":
            Department.objects.create(department_name=request.POST.get('department'))
            return render(request,"Admin/Department.html",{'res':dep})
        else:
            return render(request,"Admin/Department.html",{'res':dep})
    else:
        return redirect("guest:Logins")


def DelDepartment(request,did):
    if 'aid' in request.session:
        dep=Department.objects.get(id=did)
        dep.delete()
        return redirect("webadmin:Department")
    else:
        return redirect("guest:Logins")

def district(request):
    if 'aid' in request.session:
        dis=District.objects.all()
        if request.method=="POST":
            District.objects.create(district_name=request.POST.get('district'))
            return render(request,"Admin/District.html",{'res':dis})
        else:
            return render(request,"Admin/District.html",{'res':dis})
    else:
        return redirect("guest:Logins")

def DelDistrict(request,did):
    if 'aid' in request.session:
        dis=District.objects.get(id=did)
        dis.delete()
        return redirect("webadmin:District")
    else:
        return redirect("guest:Logins")

def complainttype(request):
    if 'aid' in request.session:
        com=Complainttype.objects.all()
        if request.method=="POST":
            Complainttype.objects.create(complaint_type=request.POST.get('complaint'))
            return render(request,"Admin/Complainttype.html",{'res':com})
        else:
            return render(request,"Admin/Complainttype.html",{'res':com})
    else:
        return redirect("guest:Logins")

def DelComplaint(request,did):
    if 'aid' in request.session:
        com=Complainttype.objects.get(id=did)
        com.delete()
        return redirect("webadmin:Complaint")
    else:
        return redirect("guest:Logins")

def hospital(request):
    if 'aid' in request.session:
        hos=Hospitaltype.objects.all()
        if request.method=="POST":
            Hospitaltype.objects.create(hospital_type=request.POST.get('hospital'))
            return render(request,"Admin/Hospitaltype.html",{'res':hos})
        else:
            return render(request,"Admin/Hospitaltype.html",{'res':hos})
    else:
        return redirect("guest:Logins")


def DelHospital(request,did):
    if 'aid' in request.session:
        hos=Hospitaltype.objects.get(id=did)
        hos.delete()
        return redirect("webadmin:Hospital")
    else:
        return redirect("guest:Logins")

def place(request):
    if 'aid' in request.session:
        dist=District.objects.all()
        pl=Place.objects.all()
        if request.method=="POST":
            d=District.objects.get(id=request.POST.get('district'))
            Place.objects.create(place_name=request.POST.get('place'),district=d)
            return render(request,"Admin/Place.html",{'district':dist,'pl':pl})
        else:
            return render(request,"Admin/Place.html",{'district':dist,'pl':pl})
    else:
        return redirect("guest:Logins")

def DelPlace(request,did):
    if 'aid' in request.session:
        pl=Place.objects.get(id=did)
        pl.delete()
        return redirect("webadmin:Place")
    else:
        return redirect("guest:Logins")

def NewHospital(request):
    if 'aid' in request.session:
        newhos=Hospital.objects.filter(status=0)
        return render(request,"Admin/NewHospitalList.html",{'data':newhos})
    else:
        return redirect("guest:Logins")


def AcceptedHospital(request):
    if 'aid' in request.session:
        ahos=Hospital.objects.filter(status=1)
        return render(request,"Admin/AcceptedHospitalList.html",{'data':ahos})
    else:
        return redirect("guest:Logins")    

def RejectedHospital(request):
    if 'aid' in request.session:
        rhos=Hospital.objects.filter(status=2)
        return render(request,"Admin/RejectedHospitalList.html",{'data':rhos})
    else:
        return redirect("guest:Logins")   

def AcceptHospital(request,aid):
    if 'aid' in request.session:
        h=Hospital.objects.get(id=aid)
        h.status=1
        h.save()
        return redirect("webadmin:newhospital")
    else:
        return redirect("guest:Logins")   



def RejectHospital(request,rid):
    if 'aid' in request.session:
        ho=Hospital.objects.get(id=rid)
        ho.status=2
        ho.save()
        return redirect("webadmin:newhospital")  
    else:
        return redirect("guest:Logins")   

def HomePage(request):
    if 'aid' in request.session:
        ad=Adminlogin.objects.get(id=request.session["aid"])
        return render(request,"Admin/HomePage.html",{'data':ad})
    else:
        return redirect("guest:Logins")  

def ViewComplaint(request): 
    if 'aid' in request.session:
      
        com=complaint.objects.filter(user__gt=0,status=0)
        comp=complaint.objects.filter(doctor__gt=0,status=0)
        compl=complaint.objects.filter(hospital__gt=0,status=0)
        return render(request,"Admin/ComplaintView.html",{'com':com,'comp':comp,'compl':compl})
    else:
        return redirect("guest:Logins") 

def ViewFeedback(request):
    if 'aid' in request.session:
       
        feed=feedback.objects.filter(user__gt=0)
        feed1=feedback.objects.filter(doctor__gt=0)
        feed2=feedback.objects.filter(hospital__gt=0)
        return render(request,"Admin/FeedbackView.html",{'feed':feed,'feed1':feed1,'feed2':feed2})
    else:
        return redirect("guest:Logins") 
    
def ComplaintReply(request,cid):
    cmp=complaint.objects.get(id=cid)
    if request.method=="POST":
        cmp.reply=request.POST.get('txtaddress')
        cmp.status=1
        cmp.save()
        return redirect("webadmin:viewcomp")
    else:
        return render(request,"Admin/Reply.html")
    
def logout(request):
    del request.session["aid"]
    return redirect("guest:Logins")

def UserList(request):
    data=NewUser.objects.all()
    return render(request,"Admin/UserList.html",{'data':data})