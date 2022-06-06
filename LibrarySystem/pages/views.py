from django import forms
from django.forms.widgets import PasswordInput
from django.shortcuts import render, redirect
from .models import addbook, Profile
from .forms import LoginForm, CreationUserForm, ProfileForm
from django.contrib.auth import authenticate, login as Login, logout as Logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required as req_Login
from .decorators import req_Login as RLogin
from django.contrib.auth.models import Group, User
from django.utils.text import slugify

# Create your views here.

def index(request):
    return render(request, 'pages/Home.html')

def login(request):
    if request.method == 'POST':
        form = LoginForm()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            profile = Profile.objects.get(name=username)
            if profile.type == 'Student':
                Login(request, user)
                return redirect('student')

            elif profile.type == 'Admin':
                Login(request, user)
                return redirect('admin')
    else:
        form = LoginForm()
    return render(request, 'pages/login.html', {'form':form})


def FormPage(request):
    if request.method == 'POST':
        form = CreationUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            gender = request.POST.get('gender')
            if request.POST.get('type') == "Admin":
                Profile(name=username, email = user.email, gender=gender, type='Admin', user=user).save()
            elif request.POST.get('type') == "Student":
                Profile(name=username, email = user.email, gender=gender, type='Student', user=user).save()
            Login(request, user)
            return redirect('Home')
    else:
        form = CreationUserForm()
    return render(request, 'pages/FormPage.html', {'form':form})



@req_Login(login_url='login')
def userLogout(request):
    Logout(request)
    return redirect('login')

@req_Login(login_url='login')
def studentAccount(request):
    profile = Profile.objects.get(user = request.user)
    return render(request, 'pages/Student.html', {'profile':profile})

@req_Login(login_url='login')
def adminAccount(request):
    return render(request, 'pages/AdminProfile.html')


@req_Login(login_url='login')
def addBook(request):
    bookname= request.POST.get('bookname')
    bookauthor= request.POST.get('bookauthor')
    ISBN= request.POST.get('ISBN')
    Year= request.POST.get('Year')
    if(bookname!=None and bookauthor!=None and ISBN!=None and Year!=None):
        addbook(bookname=bookname,bookauthor=bookauthor,ISBN=ISBN,Year=Year, available=True).save()
    return render(request, 'pages/addbook.html')


@req_Login(login_url='login')
def books(request):
    profile = Profile.objects.get(user = request.user)
    search=addbook.objects.all()
    bookname =None
    bookauthor= None
    ISBN = None
    Year= None
    if 'name' in request.GET:
        bookname= request.GET['name']
        if bookname:
            search= search.filter(bookname__icontains=bookname)
    elif 'author' in request.GET:
        bookauthor= request.GET['author']
        if bookauthor:
            search= search.filter(bookauthor__icontains=bookauthor)
    elif 'isbn' in request.GET:
        ISBN= request.GET['isbn']
        if ISBN:
            search=search.filter(ISBN__icontains=ISBN)
    elif 'publicationyear' in request.GET:
        Year=request.GET['publicationyear']
        if Year:
            search=search.filter(Year__icontains=Year)
    context = {
        'books' :search,
        'profile':profile
    }
    return render(request, 'pages/Books.html',context)


@req_Login(login_url='login')
def mybooks(request):
    profile = Profile.objects.get(user = request.user)
    search=addbook.objects.all()
    bookname =None
    bookauthor= None
    ISBN = None
    Year= None
    if 'name' in request.GET:
        bookname= request.GET['name']
        if bookname:
            search= search.filter(bookname__icontains=bookname)
    elif 'author' in request.GET:
        bookauthor= request.GET['author']
        if bookauthor:
            search= search.filter(bookauthor__icontains=bookauthor)
    elif 'isbn' in request.GET:
        ISBN= request.GET['isbn']
        if ISBN:
            search=search.filter(ISBN__icontains=ISBN)
    elif 'publicationyear' in request.GET:
        Year=request.GET['publicationyear']
        if Year:
            search=search.filter(Year__icontains=Year)
    context = {
        'books' :search,
        'profile':profile
    }
    return render(request, 'pages/myBooks.html',context)


@req_Login(login_url='login')
def adminBrowsing(request):
    profile = Profile.objects.get(user = request.user)
    context = {
        'books' : addbook.objects.all(),
        'profile':profile
    }
    return render(request, 'pages/adminbrowsing.html',context)



@req_Login(login_url='login')
def operations(request, slug):
    book_detail = addbook.objects.get(slug= slug)
    return render(request, 'pages/Operations.html', {'book_detail':book_detail})

@req_Login(login_url='login')
def myoperations(request, slug):
    book_detail = addbook.objects.get(slug= slug)
    return render(request, 'pages/myBooksOperations.html', {'book_detail':book_detail})


@req_Login(login_url='login')
def borrow(request, slug):
    book_detail = addbook.objects.get(slug= slug)
    profile = Profile.objects.get(user = request.user)
    if(request.POST.get('period') != None):
        book_detail.borrowing_period = request.POST.get('period')
        book_detail.available = False
        book_detail.borrower = profile.name
        book_detail.save()
        profile.books= book_detail
        profile.save()
        
    return render(request, 'pages/borrow.html', {'book_detail':book_detail})



@req_Login(login_url='login')
def extend(request, slug):
    book_detail = addbook.objects.get(slug= slug)
    profile = Profile.objects.get(user = request.user)
    if(request.POST.get('Days') != None and book_detail.borrower == profile.name):
        book_detail.borrowing_period = request.POST.get('Days')
        book_detail.save()
        profile.books= book_detail
        profile.save()
        
    return render(request, 'pages/extend.html')


@req_Login(login_url='login')
def returnBook(request, slug):
    book_detail = addbook.objects.get(slug= slug)
    profile = Profile.objects.get(user = request.user)
    book_detail.borrowing_period = None
    book_detail.borrower = None
    book_detail.available = True
    book_detail.save()
    profile.books= book_detail
    profile.save()
        
    return render(request, 'pages/Return.html', {'book_detail':book_detail , 'profile':profile})


@req_Login(login_url='login')
def updateBook(request, slug):
    book_detail = addbook.objects.get(slug= slug)
    if request.POST.get('bookname') != None and request.POST.get('bookauthor') != None and request.POST.get('ISBN') != None:
        book_detail.bookname= request.POST.get('bookname')
        book_detail.bookauthor= request.POST.get('bookauthor')
        book_detail.ISBN= request.POST.get('ISBN')
        book_detail.Year= request.POST.get('Year')
        book_detail.save()
        return redirect('adminBooks')
    
    return render(request, 'pages/updateBook.html', {'book_detail':book_detail})


@req_Login(login_url='login')
def updateProfile(request):
    profile_detail = Profile.objects.get(user= request.user)
    user = profile_detail.user
    if request.POST.get('username') != None and request.POST.get('email') != None:
        
        profile_detail.name= request.POST.get('username')
        profile_detail.email= request.POST.get('email')
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.save()
        profile_detail.save()
        return redirect('student')
    
    return render(request, 'pages/updateProfile.html', {'profile_detail':profile_detail})

@req_Login(login_url='login')
def updateAdminProfile(request):
    profile_detail = Profile.objects.get(user= request.user)
    user = profile_detail.user
    if request.POST.get('username') != None and request.POST.get('email') != None:
        
        profile_detail.name= request.POST.get('username')
        profile_detail.email= request.POST.get('email')
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.save()
        profile_detail.save()
        return redirect('admin')
    
    return render(request, 'pages/updateAdminProfile.html')


def contact(request):
    return render(request, 'pages/contact.html')


def aboutus(request):
    return render(request, 'pages/aboutus.html')