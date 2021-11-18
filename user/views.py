from django.contrib.auth import forms
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib import messages

# Create your views here.

def register(request):
    if request.POST == 'POST':
        form = CustomUserCreationForm()
        if form.is_valid():
            form.save()
        # messages.success(request, 'Account created successfully')

    else:
        form = CustomUserCreationForm()
        context = {
            'form': form
        }
        return render(request, 'user/register.html', context)


