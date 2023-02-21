from django.db import models

# Create your models here.
class Customers(models.Model):
    cust_name = models.TextField(max_length=100)
    cust_contact = models.TextField(max_length=10)
    cust_address = models.TextField(max_length=100)
    cust_dob = models.DateField()
    cust_gender = models.TextField(max_length=10, null=True)
    cust_username = models.TextField(max_length=100)
    cust_password = models.TextField(max_length=100)

class Customer_upload(models.Model):
    customer_name = models.TextField(max_length=100)
    customer_contact = models.TextField(max_length=10)
    customer_image = models.ImageField(upload_to='profile/')    