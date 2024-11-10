from django.http import HttpResponseForbidden
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Job
from .forms import JobForm
from account.context_processors import add_user_type
# Create your views here.
@login_required
def employer_dashboard(request):
    return render(request,'employer_dashboard.html')


@login_required
def post_job(request):
    context = add_user_type(request)
    is_company = context.get('is_company')
    if not is_company:
        return HttpResponseForbidden("You are not allowed to post a job.")

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

@login_required
def job_detail(request,job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, 'job_detail.html', {'job': job})


@login_required
def edit_job(request,job_id):
    job = get_object_or_404(Job, id=job_id)
    if job.employer != request.user:
        return HttpResponseForbidden("You are not allowed to edit this job.")

    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobForm(instance=job)
    
    return render(request, 'edit_job.html', {'form': form})

@login_required
def delete_job(request,job_id):
    job = get_object_or_404(Job, id=job_id)

    if job.employer != request.user:
        return HttpResponseForbidden("You are not allowed to delete this job.")

    if request.method == 'POST':
        job.delete()
        return redirect('job_list')
    
    return render(request, 'delete_job.html', {'job': job})
