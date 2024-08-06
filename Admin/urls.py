from django.urls import path
from  Admin import views
app_name="webadmin"
urlpatterns = [
    path('dep/', views.department,name="Department"),
    path('deldep/<int:did>', views.DelDepartment,name="deldepartment"),
    path('dis/', views.district,name="District"),
    path('deldis/<int:did>', views.DelDistrict,name="deldistrict"),
    path('com/', views.complainttype,name="Complaint"),
    path('delcom/<int:did>', views.DelComplaint,name="delcomplaint"),
    path('hos/', views.hospital,name="Hospital"),
    path('delhos/<int:did>', views.DelHospital,name="delhospital"),
    path('pla/', views.place,name="Place"),
    path('delpla/<int:did>', views.DelPlace,name="delplace"),
    path('newh/', views.NewHospital,name="newhospital"),
    path('accept/', views.AcceptedHospital,name="acceptedhospital"),
    path('reject/', views.RejectedHospital,name="rejectedhospital"),
    path('ah/<int:aid>', views.AcceptHospital,name="accepthospital"),
    path('rh/<int:rid>', views.RejectHospital,name="rejecthospital"),
    path('hp/', views.HomePage,name="Home"),
    path('viewcomp/', views.ViewComplaint,name="viewcomp"),
    path('viewfeed/', views.ViewFeedback,name="viewfeedback"),
    path('rep/<int:cid>', views.ComplaintReply,name="Reply"),
    path('userlist/', views.UserList,name="Userlist"),
     path('logout/', views.logout,name="Logout"),
]

