from django.urls import path
from . import views

urlpatterns = [
    path('addcomp/',views.addcomp,name="addcompany"),
 	path('addmob/',views.addmob,name="addmobile"),
 	path('moblist/',views.moblist,name="moblist"),
    path('mobdetail/<str:u>/',views.mobdetail,name="mobdetail"),
   	path('filtermobile/',views.filtermobile,name="filtermobile"),
   
       
]
