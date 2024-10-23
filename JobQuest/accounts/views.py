from django.shortcuts import render

# registration for job seeker
def register_seeker(request):
    return render(request,"register_seeker.html")

# registration for job provider
def register_employer(request):
    return render(request,"register_employer.html")

# login for both job_Seeker or job provider
def login(request):
    return render(request,"login.html")

# logout 
def logout(request):
    return render(request,"logout.html")

# view profile 
def profile(request):
    return render(request,"profile.html")

# edit profile 
def edit_profile(request):
    return render(request,"edit_profile.html")

