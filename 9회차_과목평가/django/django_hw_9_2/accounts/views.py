from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import get_user_model

from .forms import CustomUserCreationForm

# Create your views here.
def index(request):
    User = get_user_model()
    users = User.objects.all()
    context = {
        'users' : users,
    }
    return render(request, 'accounts/index.html', context)

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('account:index')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm()
        if form.is_vaild():
            form.save()
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/signup.html', context)