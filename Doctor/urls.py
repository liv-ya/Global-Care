from django.urls import path
from  Doctor import views
app_name="doctor"
urlpatterns = [
    path('hp/', views.HomePage,name="Home"),
    path('mp/', views.MyProfile,name="Profile"),
    path('ep/', views.EditProfile,name="EProfile"),
    path('cp/', views.ChangePassword,name="CPass"),
    path('viewappointments/', views.UserAppointments,name="Viewappoint"),
    path('consult/<int:aid>', views.UserConsulted,name="consulted"),
    path('viewconsulted/', views.ViewConsulted,name="Viewconsult"),
    path('medicinereport/<int:mid>', views.UpMediReport,name="medireport"),
    path('prescribtion/<int:pid>', views.AddPrescribtion,name="prescribe"),
    path('viewHis/<int:hid>', views.ViewHistory,name="ViewHist"),
    path('cv/', views.Sendcomplaint,name="Complaint"),
    path('delcom/<int:cid>', views.DelComplaint,name="delcomplaint"),
    path('feed/', views.SendFeedBack,name="Feedback"),
    path('delfee/<int:cid>', views.DelFeedback,name="delfeedback"),
    path('logout/', views.logout,name="Logout"),
   
]
