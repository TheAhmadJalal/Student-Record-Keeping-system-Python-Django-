from import_export import resources
from AspireApp.models import Student

class StudentResource(resources.ModelResource):
    class meta:
        model= Student
