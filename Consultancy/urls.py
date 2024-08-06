from django.urls import path
from  Consultancy import views
app_name="consultancy"

urlpatterns = [
    path('hp/', views.HomePage,name="Home"),
    path('mp/', views.MyProfile,name="Profile"),
    path('ep/', views.EditProfile,name="EProfile"),
    path('cp/', views.ChangePassword,name="CPass"),
    path('vd/', views.ViewDoctors,name="VD"),
    path('setavailability/<int:did>',views.SetAvailability,name="setavailability"),
    path('token/<int:did>',views.gentoken,name="gentoken"),
    path('viewapp/', views.UserAppointment,name="Viewappoint"),
    path('accept/', views.AcceptAppointment,name="Acceptappoint"),
    path('reject/', views.RejectAppointment,name="Rejectappoint"),
    path('aa/<int:aid>', views.AcceptedAppointement,name="acceptappointment"),
    path('ra/<int:rid>', views.RejectededAppointement,name="rejectappointment"),
    path('cancelappoint/<int:aid>', views.AppointmentCancel,name="Cancelappoint"),
    path('logout/', views.logout,name="Logout"),
   
]
