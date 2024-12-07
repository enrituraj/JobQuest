from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def my_application(request):
    return render(request,'my_application.html')

@login_required
def apply_job(request,job_id):
    return render(request,'apply_job.html')
