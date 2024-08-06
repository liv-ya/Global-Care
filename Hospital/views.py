from django.shortcuts import render,redirect
from Guest.models import Hospital
from Admin.models import Department
from Hospital.models import  *
# Create your views here.

def HomePage(request):
    if 'hid' in request.session:
        ho=Hospital.objects.get(id=request.session["hid"])
        return render(request,"Hospital/HomePage.html",{'data':ho})
    else:
        return redirect("guest:Logins")

def MyProfile(request):
    if 'hid' in request.session:
        hos=Hospital.objects.get(id=request.session["hid"])
        return render(request,"Hospital/MyProfile.html",{'hos':hos})
    else:
        return redirect("guest:Logins")

def EditProfile(request):
    if 'hid' in request.session:
        ho=Hospital.objects.get(id=request.session["hid"])
        if request.method=="POST":
            ho.name=request.POST.get('txtname')
            ho.contact=request.POST.get('txtnumber')
            ho.address=request.POST.get('txtaddress')
            ho.save()
            return redirect("hospital:Profile")
        else:
            return render(request,"Hospital/EditProfile.html",{'ho':ho})
    else:
        return redirect("guest:Logins")

def ChangePassword(request):
    if 'hid' in request.session:
        if request.method=="POST":
            hoscount=Hospital.objects.filter(id=request.session["hid"],password=request.POST.get('txtpassword1')).count()
            if hoscount>0:
                hospital=Hospital.objects.get(id=request.session["hid"],password=request.POST.get('txtpassword1'))
                hospital.password=request.POST.get('txtpassword2')
                hospital.save()
                return redirect("hospital:Home")
            else:
                return redirect("hospital:CPass")
        else:   
            return render(request,"Hospital/ChangePassword.html")
    else:
        return redirect("guest:Logins")


def NewConsultancy(request):
    if 'hid' in request.session:
        ho=Hospital.objects.all()
        if request.method=="POST":
            hos=Hospital.objects.get(id=request.session['hid'])
            Consultancy.objects.create(name=request.POST.get('txtname'),email=request.POST.get('txtemail'),headname=request.POST.get('txtheadname'),password=request.POST.get('txtpass'),hospital_id=hos)
            return render(request,"Hospital/NewConsultancy.html",{'ho':ho})
        else:
            return render(request,"Hospital/NewConsultancy.html",{'ho':ho})
    else:
        return redirect("guest:Logins")


def newDoctor(request):
    if 'hid' in request.session:
        dept=Department.objects.all()
        hos=Hospital.objects.all()
        if request.method=="POST":
            de=Department.objects.get(id=request.POST.get('txtdepartment'))
            hos=Hospital.objects.get(id=request.session['hid'])
            Doctor.objects.create(name=request.POST.get('txtname'),contact=request.POST.get('txtnumber'),email=request.POST.get('txtemail'),address=request.POST.get('txtaddress'),photo=request.FILES.get('txtphoto'),proof=request.FILES.get('txtproof'),department=de,hospital=hos,password=request.POST.get('txtpass'),gender=request.POST.get('txtgender'))
            return render(request,"Hospital/NewDoctor.html",{'dept':dept,'hos':hos})
        else:
            return render(request,"Hospital/NewDoctor.html",{'dept':dept,'hos':hos})
    else:
        return redirect("guest:Logins")


def Sendcomplaint(request):
    if 'hid' in request.session:
        nu=int(request.session["hid"])
        ctype=Complainttype.objects.all()
        dt=complaint.objects.filter(hospital=nu)
        if request.method=="POST":
            com=Complainttype.objects.get(id=request.POST.get('complaint_type'))
            complaint.objects.create(typeid=com,title=request.POST.get('txttit'),content=request.POST.get('txtcont'),hospital=nu)
            return render(request,"Hospital/Complaint.html",{'data':dt,'complaint_type':ctype})
        else:
            return render(request,"Hospital/Complaint.html",{'data':dt,'complaint_type':ctype})
    else:
        return redirect("guest:Logins")

def DelComplaint(request,cid):
    if 'hid' in request.session:
        com=complaint.objects.get(id=cid)
        com.delete()
        return redirect("hospital:Home")
    else:
        return redirect("guest:Logins")

def SendFeedBack(request):
    if 'hid' in request.session:
        nu=int(request.session["hid"])
        dt=feedback.objects.filter(hospital=nu)
        if request.method=="POST":
            feedback.objects.create(content=request.POST.get('txtmedi'),hospital=nu)
            return render(request,"Hospital/Feedback.html",{'dt':dt})
        else:
            return render(request,"Hospital/Feedback.html",{'dt':dt})
    else:
        return redirect("guest:Logins")

def DelFeedback(request,cid):
    if 'hid' in request.session:
        com=feedback.objects.get(id=cid)
        com.delete()
        return redirect("hospital:Home")
    else:
        return redirect("guest:Logins")
    
def logout(request):
    del request.session["hid"]
    return redirect("guest:Logins")