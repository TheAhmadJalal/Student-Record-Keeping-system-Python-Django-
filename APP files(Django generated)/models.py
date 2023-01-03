import email
from pickle import TRUE
from xml.etree.ElementInclude import default_loader
from django.db import models

# Create your models here.

class Student(models.Model):
    Sr_No = models.IntegerField(primary_key=True, default=0)
    St_name= models.CharField(max_length=30,null=True,default=0)
    F_name= models.CharField(max_length=30,null=True,default=0)
    DOB= models.CharField(max_length=10,null=True,default=0)#################
    Gender= models.CharField(max_length=10,null=True,default=0)
    B_Form= models.CharField(null=True,max_length=30,default=0)
    St_Mobile= models.CharField(max_length=20,null=True,default=0)
    F_Cnic = models.CharField(max_length=20,null=True,default=0)
    F_Mobile = models.CharField(max_length=20,null=True,default=0)
    DateOfAdmission= models.CharField(max_length=10,null=True,default=0)########################
    Program= models.CharField(max_length=20,null=True,default=0)
    Package= models.IntegerField(null=True,default=0)
    First_Installment= models.IntegerField(null=True,default=0)
    Matric_RollNo= models.CharField(max_length=10,null=True, default=0)
    Matric_Marks= models.CharField(max_length=5,null=True, default=0)
    Admisson_By= models.CharField(max_length=40,null=True, default=0)
    Approached_By= models.CharField(max_length=40, null=True, default=0)
    Entered_By= models.CharField(max_length=30,null=True,default=0)
    Status= models.CharField(max_length=10,null=True,default=0)
 