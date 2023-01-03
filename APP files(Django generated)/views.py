from operator import imod
from django.shortcuts import redirect
from turtle import title
from urllib import request
from django.shortcuts import render
from AspireApp.models import Student
from .resources import StudentResource
from django.http import HttpResponse,HttpResponseRedirect
from tablib import Dataset
from django.contrib import messages
from .resources import StudentResource
from django.template import loader
# Create your views here.
def index(request):
    return render(request, 'index.html')

def simple_upload(request):
    
    if request.method == 'POST':
        student_resource = StudentResource()
        dataset = Dataset()
        new_student = request.FILES['myfile']
        
        if not new_student.name.endswith('xlsx'):
            messages.info(request,'wrong format')
            return render(request,'upload.html')
               
        imported_data = dataset.load(new_student.read(),format='xlsx')
        #print(imported_data)
        for data in imported_data:
                value = Student(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15],data[16],data[17],data[18])
                value.save()
            
    return render(request, 'upload.html')

def getData(request):
    allStudents= Student.objects.all()
    context= {'Stds':allStudents}
    return render(request,'FetchData.html',context)

def Search(request):
    return render(request,'Search.html')

def SearchByStatus(request):
    return render(request,'SearchByStatus.html')


def SearchByBForm(request):
    return render(request,'SearchByBForm.html')

def SearchResult(request):
    Search_Student = request.GET['Search_Student']
    
    if len(Search_Student)>78 or len(Search_Student)<1: 
        allStudents=Student.objects.none()
        # print(allStudents.count())
    else:        
        allStudents = Student.objects.filter(St_name__icontains=Search_Student)
        
    if allStudents.count()==0 and len(Search_Student)==0:
        messages.warning(request, "No search results found. Please refine your Search.")
        return render(request,'Search.html')
        
    context= {'Stds':allStudents , 'Search_Student':Search_Student}
    return render(request,'SearchResults.html', context)
                              
def SearchResultsViaStatus(request):
    Search_Student = request.GET['Search_Student']
    
    if len(Search_Student)>78 or len(Search_Student)<1: 
        allStudents=Student.objects.none()
        # print(allStudents.count())
    else:        
        allStudents = Student.objects.filter(Status__icontains=Search_Student)
        
    if allStudents.count()==0 and len(Search_Student)==0:
        messages.warning(request, "No search results found. Please refine your Search.")
        return render(request,'Search.html')
        
    context= {'Stds':allStudents , 'Search_Student':Search_Student}
    return render(request,'SearchResults.html', context)

def SearchResultsViaBForm(request):
    Search_Student = request.GET['Search_Student']
    
    if len(Search_Student)>78 or len(Search_Student)<1: 
        allStudents=Student.objects.none()
        # print(allStudents.count())
    else:        
        allStudents = Student.objects.filter(B_Form__icontains=Search_Student)
        
    if allStudents.count()==0 and len(Search_Student)==0:
        messages.warning(request, "No search results found. Please refine your Search.")
        return render(request,'Search.html')
        
    context= {'Stds':allStudents , 'Search_Student':Search_Student}
    return render(request,'SearchResults.html', context)
    

def AddStudent(request):
    
    if request.method == "POST":
        St_name = request.POST.get('St_name')
        F_name = request.POST.get('F_name')
        DOB = request.POST.get('DOB')
        Gender = request.POST.get('Gender')
        B_Form = request.POST.get('B_Form')
        St_Mobile = request.POST.get('St_Mobile')
        F_Cnic = request.POST.get('F_Cnic')
        F_Mobile = request.POST.get('F_Mobile')
        DateOfAdmission = request.POST.get('DateOfAdmission')
        Program = request.POST.get('Program')
        Package = request.POST.get('Package')
        First_Installment = request.POST.get('First_Installment')
        Matric_RollNo = request.POST.get('Matric_RollNo')
        Matric_Marks = request.POST.get('Matric_Marks')
        Admisson_By = request.POST.get('Admisson_By')
        Approached_By = request.POST.get('Approached_By')
        Entered_By = request.POST.get('Entered_By')
        Status = request.POST.get('Status')
        
        
        student = Student(St_name=St_name,F_name=F_name,DOB=DOB,Gender=Gender,B_Form=B_Form,
                          St_Mobile=St_Mobile,F_Cnic=F_Cnic,F_Mobile=F_Mobile,
                          DateOfAdmission=DateOfAdmission,Program=Program,Package=Package,
                          First_Installment=First_Installment,Matric_RollNo=Matric_RollNo,
                          Matric_Marks=Matric_Marks,Admisson_By=Admisson_By,
                          Approached_By=Approached_By,Entered_By=Entered_By,Status=Status
                          )
        
        student.save()
        
        messages.success(request, 'Successfully entered the student.')
        
    return render(request,'AddStudent.html')

def DeleteRecord(request,id,id2):
    try:
        Std = Student.objects.get(pk=id2)
        Std.delete()
        messages.warning(request, "Successfully Deleted a Record.")
       
    except:
        pass
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def Update(request,id,id2): 
    print('aaaaaaaaa')
    Std = Student.objects.get(pk=id)
    print(Std)
    # template = loader.get_template('update.html')
    context= {'Stds':Std , 'search_string':id2}
    return render(request,'update.html', context)

def UpdateRecord(request, id , id2):
    
    # if request.method == "POST":
    # SrNo = request.POST.get('Sr_No')
    
    Stname = request.POST.get('St_name')
    print(Stname)
    Fname = request.POST.get('F_name')
    DOB1 = request.POST.get('DOB')
    Gender1 = request.POST.get('Gender')
    BForm = request.POST.get('B_Form')
    StMobile = request.POST.get('St_Mobile')
    FCnic = request.POST.get('F_Cnic')
    FMobile = request.POST.get('F_Mobile')
    DateOfAdmission1 = request.POST.get('DateOfAdmission')
    Program1 = request.POST.get('Program')
    Package1 = request.POST.get('Package')
    FirstInstallment = request.POST.get('First_Installment')
    print(FirstInstallment)
    MatricRollNo = request.POST.get('Matric_RollNo')
    MatricMarks = request.POST.get('Matric_Marks')
    AdmissonBy = request.POST.get('Admisson_By')
    ApproachedBy = request.POST.get('Approached_By')
    EnteredBy = request.POST.get('Entered_By')
    Status1 = request.POST.get('Status')
        
    std = Student.objects.get(pk=id)
    # std.Sr_No = id
    std.St_name = Stname
    std.F_name = Fname
    std.DOB = DOB1
    std.Gender = Gender1
    std.B_Form = BForm
    std.St_Mobile = StMobile
    std.F_Cnic = FCnic
    std.F_Mobile = FMobile
    std.DateOfAdmission = DateOfAdmission1
    std.Program = Program1
    std.Package = Package1
    std.First_Installment =FirstInstallment
    std.Matric_RollNo = MatricRollNo
    std.Matric_Marks = MatricMarks
    std.Admisson_By = AdmissonBy
    std.Approached_By = ApproachedBy
    std.Entered_By = EnteredBy
    std.Status = Status1
  
    std.save()
    
    # allStudents = Student.objects.filter(St_name__icontains=id2)
    # context= {'Stds':allStudents , 'Search_Student':Stname}
    # return render(request,'SearchResults.html', context)
    
    messages.success(request, "Successfully Updated a Record.")
    return render(request, 'index.html')