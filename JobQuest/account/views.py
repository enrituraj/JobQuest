from django.shortcuts import render,redirect
from .forms import UserRegistrationForm,CustomLoginForm,EditProfileForm,PasswordChangeForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.models import User

# registration for job seeker
def register_seeker(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                messages.error(request, "An account with this email already exists.")
            else:    
                user = form.save(commit=False)
                user.set_password(form.cleaned_data['password1'])
                user.save()
                login(request,user)
                return redirect('login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{error}")
    else:
        form = UserRegistrationForm()
    return render(request,"register_seeker.html",{'form':form})

# registration for job provider
def register_employer(request):
    return render(request,"register_employer.html")

# login for both job_Seeker or job provider
def not_logged_in(user):
    return not user.is_authenticated

@user_passes_test(not_logged_in, login_url='home')
def custom_login(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # redirect to home or desired page after login
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = CustomLoginForm()
    return render(request,"login.html",{'form':form})

# logout 
@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect(settings.LOGOUT_REDIRECT_URL or 'login')

# view profile 
@login_required
def profile(request):
    user = request.user
    return render(request,"profile.html",{'user':user})

# edit profile 
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, "Your profile has been updated successfully.")
            return redirect('profile')
    else:
        form = EditProfileForm(instance = request.user)
    return render(request,"edit_profile.html",{'form':form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user out after changing password
            messages.success(request, "Your password has been changed successfully. Please log in again.")
            return redirect('login')  # Redirect to the login page
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, "change_password.html", {'form': form})