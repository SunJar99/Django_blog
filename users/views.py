from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm , UserUpdateForm, ProfileUpdateform
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:

        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def profile(request):

    u_form = UserUpdateForm()
    p_form = ProfileUpdateform()

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)