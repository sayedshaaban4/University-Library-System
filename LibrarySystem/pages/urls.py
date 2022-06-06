from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('', views.userLogout, name='logout'),
    path('login', views.login, name='login'),
    path('FormPage', views.FormPage, name='FormPage'),
    path('AddBook', views.addBook, name='addbook'),
    path('Student', views.studentAccount, name='student'),
    path('Admin', views.adminAccount, name='admin'),
    path('Books/', views.books, name='Books'), 
    path('MyBooks/', views.mybooks, name='mybooks'),  
    path('adminBooks/', views.adminBrowsing, name='adminBooks'),  
    path('Borrow/<slug:slug>', views.borrow, name='borrow'), 
    path('Return/<slug:slug>', views.returnBook, name='returnBook'),
    path('MyBooksOperations/<slug:slug>', views.myoperations, name='myoperations'),   
    path('Extend/<slug:slug>', views.extend, name='extend'),  
    path('<slug:slug>/', views.operations, name='operations'), 
    path('UpdateBook/<slug:slug>', views.updateBook, name='updateBook'), 
    path('UpdateProfile', views.updateProfile, name='updateProfile'),
    path('UpdateAdminProfile', views.updateAdminProfile, name='updateAdminProfile'),
    path('contact',views.contact,name='contact'),
    path('aboutus',views.aboutus,name='aboutus'),
]

