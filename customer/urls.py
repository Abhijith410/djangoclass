from django.urls import path
from . import views
app_name = 'cust'

urlpatterns = [
    path('sum/',views.addnumbers, name = "sum"),
    path('registration', views.addcustomer, name = "reg"),
    path('table/', views.getcustomers, name = "data"),
    path('delete/<int:cust_id>',views.deleterow, name = "delete_customer"),
    path('update/<int:cust_id>',views.updaterow, name = "update_customer"),
    path('upload/', views.uploadimage, name="image"),
    path('display/', views.displayprofile, name = "display"),
    path('login/', views.login, name = "login"),
    path('customerhome/', views.home, name = "homepage"),
    path('logoutcustomer', views.customer_logout, name = "logout"),
    path('checkusernameavailable/', views.customer_usercheck, name ="usernamecheck"),
    path('apicustomerregister/', views.apicustregister, name = "cregister"),
    path('apigetcustomer/', views.apigetcustomers, name = "apigetcustomer")    
]