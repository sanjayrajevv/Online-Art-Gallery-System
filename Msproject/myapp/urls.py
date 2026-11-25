from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.showhomepage),
    path('h/',views.showhomepage),
    path('lp/',views.login),
    path('p/',views.paintings),
    path('l/',views.Gallery),

    path('sap/',views.showadminpage),
    path('adp/',views.addproduct),
    path('ap/',views.listproduct),
    path('del/<int:id>/',views.delprogram),
    path('ed/<int:id>/',views.editproduct),


    path('pp/',views.registration),
    path('bb/',views.login),
    path('au/',views.about),
    path('c/',views.contact),
    path('sup/',views.showuserpage),
    path('atoc/<int:id>/',views.order),
    path('vc/', views.viewcart),
    path('delp/<int:id>/', views.removeitem),
    path('pay/', views.payment),
    path('upay/', views.userpayment),

    path('passs/', views.changepassword),
    path('myp/', views.viewsales),
    path('ms/<int:salesno>/', views.viewsalessub),
    path('nfeed/', views.addfeedback),
    path('vfd/', views.viewfeedback),

    path('inv/', views.adminviewsales),
    path('ams/<int:salesno>/', views.adminviewsalessub),
    path('ams1/<int:salesno>/', views.invoice),

    path('adms/',views.adminsaleshistory),


]