from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UserRegisterForm

# Create your views here.


@login_required
def profile(request):
    return render(request, 'users/user_profile.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('posts:index')

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created.')
            return redirect('users:login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/user_register.html', {'form': form})
