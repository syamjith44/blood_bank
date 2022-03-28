from django.contrib import auth, messages
from django.shortcuts import render, redirect
from .models import Center, Doner
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.http import JsonResponse




def home(request):
    users = User.objects.all()
    count = 1200 + len(users)

    return render(request, 'index.html', {'count': count})


def create_account(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        re_password = request.POST['re_password']

        if password == re_password:
            if User.objects.filter(email=email).exists():
                messages.info(request, "You already have an account with this email")
                return redirect('myapp:create_account')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "username not available")
                return redirect('myapp:create_account')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

        else:
            messages.info(request, "passwords does not match")
            return redirect('myapp:create_account')

        return redirect('myapp:login')
    return render(request, 'create_account.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            print('user logged in')
        else:
            messages.info(request, "invalid login credentials")
            return redirect('myapp:login')

        return redirect('myapp:register')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myapp:thanks')

    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


def load_centers(request):
    district_id = request.GET.get('district')
    centers = Center.objects.filter(district_id=district_id).order_by('name')
    return render(request, 'center_dropdown_list_options.html', {'centers': centers})


def thanks(request):
    return render(request, 'thanks.html')
