
from django.urls import path
from .views import employer_dashboard,post_job,job_list

urlpatterns = [
    path('',employer_dashboard,name="employer_dashboard"),
    path('post_job/',post_job,name="post_job"),
    path('job_list/',job_list,name="job_list"),
]
