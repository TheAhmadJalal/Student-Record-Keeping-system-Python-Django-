"""Aspire_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from AspireApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('simple_upload',views.simple_upload),
    path('getData',views.getData),
    
    path('Search',views.Search),
    path('SearchResults',views.SearchResult),
    
    path('SearchByBForm',views.SearchByBForm),
    path('SearchResultsViaBForm',views.SearchResultsViaBForm),
    
    path('SearchByStatus',views.SearchByStatus),
    path('SearchResultsViaStatus',views.SearchResultsViaStatus),
    
    path('AddStudent',views.AddStudent),
    path('DeleteRecord/<id>/<id2>',views.DeleteRecord,name='delete-record'),
    
    path('UpdateRecord/<int:id>/<id2>', views.UpdateRecord, name='updaterecord'),
    path('Update/<id>/<id2>',views.Update,name='update'),
    
    
   
]
