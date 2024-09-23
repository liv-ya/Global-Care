from django.urls import path
from  User import views
app_name="user"
urlpatterns = [
     path('uhp/', views.HomePage,name="Home"),
     path('mp/', views.MyProfile,name="Profile"),
     path('ep/', views.EditProfile,name="EProfile"),
     path('cp/', views.ChangePassword,name="CPass"),
     path('sh/', views.SearchHospital,name="Sh"),
     path('viewdoc/<int:hid>', views.ViewDoctor,name="viewd"),
     path('viewavail/<int:did>', views.ViewAvailability,name="viewa"),
     path('viewslot/<int:did>', views.ViewSlot,name="views"),
     path('ajaxhos/', views.AjaxHos,name="Ajax-hos"),
     path('ajaxdoc/', views.AjaxDoc,name="Ajax-doctor"),
     path('ca/<int:sid>', views.ConfirmAppointment,name="ca"),
     path('viewapp/', views.UserAppointment,name="Viewappoint"),
     path('viewpre/<int:pid>', views.ViewPrescrib,name="viewpres"),
     path('cv/', views.Sendcomplaint,name="Complaint"),
     path('delcom/<int:cid>', views.DelComplaint,name="delcomplaint"),
     path('feed/', views.SendFeedBack,name="Feedback"),
     path('delfee/<int:cid>', views.DelFeedback,name="delfeedback"),   
     path('viewmed/<int:mid>', views.ViewMedical,name="viewmedical"),
     path('print/', views.PrintApp,name="PrintAppointment"),
     path('logout/', views.logout,name="Logout"),
]
