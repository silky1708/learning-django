from django.shortcuts import render, redirect
from .models import Feature
from django.contrib.auth.models import User, auth
from django.contrib import messages
# from django.http import HttpResponse

# Create your views here.
def index(request):
    # context = {
    #     'name': 'Silky',
    #     'age': 21,
    #     'nationality': 'Indian'
    # }

    # feature1 = Feature()
    # feature1.id = 0
    # feature1.name = 'Fast'
    # feature1.details = 'Our service is very quick'

    # once added to DB, no need to define them manually
    features = Feature.objects.all() ## list
    return render(request, 'index.html', {'features': features})

def counter(request):
    words = request.POST['words']
    numWords = len(words.split(' '))
    return render(request, 'counter.html', {'numWords': numWords})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_reentered = request.POST['password_reenter']

        if password == password_reentered:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already in use!')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already in use!')
                return redirect('register')
            else:
                # create a user
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')

        else:
            messages.info(request, "Passwords don't match")
            return redirect('register')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get('username', "")
        password = request.POST.get('password', "")

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Username or password incorrect.")
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')