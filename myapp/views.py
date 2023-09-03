from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import place,Explore
from django.core.mail import send_mail
from django.http import JsonResponse




# Create your views here.
@login_required(login_url='signin')
def home(request):
    places=place.objects.all()
    explore_places=Explore.objects.all()
    return render(request,'home.html',{'places':places,'explore':explore_places})

def signup(request): 
    if request.method == 'POST':
        username = request.POST['fullname']
        email = request.POST['email']
        password = request.POST['password']      
        if username=='' or email=='' or password=='': 
            messages.error(request,'please enter all the fields')
            return redirect('/')
        # Check if username or email already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('/')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return redirect('/')
        
        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('home')
    else:
        return render(request, 'signup.html')
def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        if username=='' or password=='':
            messages.error(request,'please fill all the details')
            return redirect('signin')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
            # next_url = request.GET.get('next', '/home')
            # return redirect(next_url)
        else:
            messages.error(request,'invalid credentials')
            return redirect('signin')
    else:
        return render(request,'signin.html')
def logout(request):
    auth.logout(request)
    return redirect('signin')
def detail(request,pk):
    post=place.objects.get(id=pk)
    return render(request,'detail.html',{'post':post})
def explore(request,pk):
    explore_p=Explore.objects.get(id=pk)
    return render(request,'explore.html',{'explores':explore_p})
# def bookh(request):  
def bookh(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        card = request.POST.get('card')
        expiry = request.POST.get('expiry')
        cvv = request.POST.get('cvv')
        terms = request.POST.get('terms')

        response_data = {'message': 'Form submitted successfully!'}
        return JsonResponse(response_data)
    else:
        return render(request,'book.html')


