from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from AspireApp.models import Student
# Register your models here.

@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    list_display= ('St_name','F_name','DOB','Gender','B_Form','St_Mobile','F_Cnic' ,'F_Mobile',
                    'DateOfAdmission',
                    'Program',
                    'Package',
                    'First_Installment',
                    'Matric_RollNo',
                    'Matric_Marks',
                    'Admisson_By',
                    'Approached_By',
                    'Entered_By',
                    'Status',
                   )