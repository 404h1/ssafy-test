from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import get_user_model  # 유저 목록 가져오려면 필요함
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
            return redirect('accounts:index')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)