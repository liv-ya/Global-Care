from django.urls import path
from  Guest import views
app_name="guest"

urlpatterns = [
    path('',views.home,name="Home"),
    path('hospital/', views.hospital,name="Hospital"),
    path('newu/', views.newuser,name="Newuser"),
    path('ajaxpla/', views.Ajaxpla,name="Ajax-Place"),
    path('login/', views.Login,name="Logins"),
    path('fpass/', views.ForgetPassword,name="forpass"),
    path('otpver/', views.OtpVerification,name="verification"),
    path('create/', views.CreateNewPass,name="create"),
    
   
]
