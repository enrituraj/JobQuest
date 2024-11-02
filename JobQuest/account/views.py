from django.shortcuts import render,redirect
from .forms import UserRegistrationForm,CustomLoginForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.conf import settings

# registration for job seeker
def register_seeker(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request,"register_seeker.html",{'form':form})

# registration for job provider
def register_employer(request):
    return render(request,"register_employer.html")

# login for both job_Seeker or job provider
def custom_login(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')  # redirect to home or desired page after login
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = CustomLoginForm()
    return render(request,"login.html",{'form':form})

# logout 
def logout_view(request):
    logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL or 'login')

# view profile 
@login_required
def profile(request):
    user = request.user
    return render(request,"profile.html",{'user':user})

# edit profile 
def edit_profile(request):
    return render(request,"edit_profile.html")

