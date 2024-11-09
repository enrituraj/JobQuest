
from django.urls import path
from .views import employer_dashboard,post_job,job_list,job_detail,edit_job,delete_job

urlpatterns = [
    path('',employer_dashboard,name="employer_dashboard"),
    path('post_job/',post_job,name="post_job"),
    path('job_list/',job_list,name="job_list"),
    path('<int:job_id>/details/',job_detail,name="job_detail"),
    path('<int:job_id>/edit/',edit_job,name="edit_job"),
    path('<int:job_id>/delete/',delete_job,name="delete_job"),
]
