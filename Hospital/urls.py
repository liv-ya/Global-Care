from django.urls import path
from  Hospital import views
app_name="hospital"
urlpatterns = [
    path('hp/', views.HomePage,name="Home"),
    path('mp/', views.MyProfile,name="Profile"),
    path('ep/', views.EditProfile,name="EProfile"),
    path('cp/', views.ChangePassword,name="CPass"),
    path('con/', views.NewConsultancy,name="NewCon"),
    path('doc/', views.newDoctor,name="NewDoc"),
    path('cv/', views.Sendcomplaint,name="Complaint"),
    path('delcom/<int:cid>', views.DelComplaint,name="delcomplaint"),
    path('feed/', views.SendFeedBack,name="Feedback"),
    path('delfee/<int:cid>', views.DelFeedback,name="delfeedback"),
    path('logout/', views.logout,name="Logout"),
    
]
