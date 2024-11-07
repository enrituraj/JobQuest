from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Job
from .forms import JobForm

# Create your views here.
@login_required
def employer_dashboard(request):
    return render(request,'employer_dashboard.html')


@login_required
def post_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.employer = request.user  # Set the current user as the employer
            job.save()
            return redirect('job_list')  # Redirect to a job listing or confirmation page
    else:
        form = JobForm()
    return render(request, 'post_job.html', {'form': form})

@login_required
def job_list(request):
    jobs = Job.objects.all().order_by('-created_at')
    return render(request, 'job_list.html', {'jobs': jobs})
