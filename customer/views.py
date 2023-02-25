from django.shortcuts import render,redirect
from . models import *
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
def addnumbers(request):
    if request.method == "POST":
        number1 = int(request.POST['num1'])
        number2 = int(request.POST['num2'])
        result = number1 + number2
        return render (request, "customer/sum.html", {'res':result})
    return render (request,"customer/sum.html")

def addcustomer(request):
    message = ""
    if request.method == "POST":
        name1 = request.POST['name']
        contact = request.POST['number']
        c_address = request.POST['address']
        c_dob = request.POST['dob']
        c_gender = request.POST['gender']
        c_username = request.POST['username']
        c_password = request.POST['password']
        customer_data = Customers(cust_name = name1, cust_contact = contact, cust_address = c_address, cust_dob = c_dob, cust_gender = c_gender, cust_username = c_username, cust_password = c_password)
        customer_data.save()
        if customer_data:
            message = "data inserted successfully"
        else:
            message = "error"    
    return render (request, "customer/customer_registration.html",{'msg':message})
    
def getcustomers(request):    
    customer_data = Customers.objects.all()
    return render (request,"customer/tables.html", {'cust_data':customer_data})

def deleterow(request,cust_id):
    Customers.objects.get(id = cust_id).delete()
    return redirect ('cust:data')    

def updaterow(request,cust_id):
    if request.method == 'POST':
        name2 = request.POST['name']
        contact2 = request.POST['number']
        c_address2 = request.POST['address']
        c_dob2 = request.POST['dob']
        c_gender2 = request.POST['gender']
        Customers.objects.filter(id=cust_id).update(cust_name = name2, cust_contact = contact2, cust_address = c_address2, cust_dob = c_dob2, cust_gender = c_gender2)
        return redirect ('cust:data')
    else:
        cust_data = Customers.objects.get(id = cust_id)
        return render (request, "customer/customer_update.html", {'cust': cust_data})   

def uploadimage(request):
    message = ""    
    if request.method == 'POST':
        customername = request.POST['name']
        customercontact = request.POST['contact']
        customerimage = request.FILES['image']
        customer_data = Customer_upload(customer_name = customername, customer_contact = customercontact, customer_image = customerimage)
        customer_data.save()
        if customer_data:
            message = "File uploaded successfully"
        else:
            message = "error"    
    return render (request, "customer/upload_customer.html", {'message':message})

def displayprofile(request):
    Customer_data = Customer_upload.objects.all()
    return render (request, "customer/file_display.html", {'cus_data':Customer_data})    

def login(request):
    if request.method == 'POST':
        user_name = request.POST['username']
        pass_word = request.POST['password']
        try:
            customer = Customers.objects.get(cust_username = user_name, cust_password = pass_word)
            request.session['customer_id'] = customer.id
            return redirect ('cust:homepage')
        except Customers.DoesNotExist:
            return render (request, "customer/customer_login.html", {'failed':'Login credentials incorrect'}) 
               
    return render (request, "customer/customer_login.html")

def home(request):
    if 'customer_id' in request.session:
        c_id = request.session['customer_id']
        customer = Customers.objects.get(id = c_id)
        return render (request, "customer/customer_home.html", {'customer_data':customer})
    
    else:
        return render (request, "customer/customer_login.html")

def customer_logout(request):
    del request.session['customer_id']
    return redirect ('cust:login')

def customer_usercheck(request):
    username = request.POST['customer_username']
    user = Customers.objects.filter(cust_username = username).exists()
    if user:
        return JsonResponse({'is_available': True})
    else:
        return JsonResponse({'is_available': False})

@api_view(['POST'])
def apicustregister(request):
    params = request.data
    customer = Customers(cust_name = params['c_name'],cust_contact = params['c_contact'],cust_address = params['c_address'],cust_dob = params['c_dob'],cust_gender = params['c_gender'],cust_username = params['c_username'],cust_password = params['c_password'])
    customer.save()
    return JsonResponse({'message': 'data inserted successfully'})

@api_view(['GET'])
def apigetcustomers(request):
    customers = Customers.objects.all()
    data = [{'id': c.id, 'name': c.cust_name, 'contact': c.cust_contact, 'address': c.cust_address, 'dob': c.cust_dob, 'gender': c.cust_gender, 'username': c.cust_username, 'password': c.cust_password } for c in customers]
    return JsonResponse({'Customer_details': data}) 