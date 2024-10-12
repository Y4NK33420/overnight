# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, LoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Existing code...
        else:
            print(form.errors)  # Print errors to console for debugging
            messages.error(request, 'Unsuccessful registration. Invalid information.')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def phone_verify_view(request):
    if request.method == 'POST':
        entered_code = request.POST.get('verification_code')
        actual_code = request.session.get('verification_code')
        user_id = request.session.get('user_id')
        if entered_code == actual_code:
            user = User.objects.get(id=user_id)
            profile = user.profile
            profile.phone_verified = True
            profile.save()
            login(request, user)
            messages.success(request, 'Phone number verified successfully.')
            # Clean up session variables
            del request.session['verification_code']
            del request.session['user_id']
            return redirect('home')
        else:
            messages.error(request, 'Invalid verification code.')
    return render(request, 'phone_verify.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.profile.phone_verified:
                    login(request, user)
                    messages.info(request, f'You are now logged in as {username}.')
                    return redirect('home')
                else:
                    messages.error(request, 'Phone number not verified. Please verify your phone number.')
                    # Redirect to phone verification
                    request.session['user_id'] = user.id
                    return redirect('phone_verify')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, 'You have successfully logged out.')
    return redirect('login')

@login_required
def home_view(request):
    return render(request, 'home.html')
