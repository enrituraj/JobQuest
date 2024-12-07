
from django.urls import path
from .views import my_application,apply_job

urlpatterns = [
    path('my_application/',my_application,name="my_application"),
    path('<int:job_id>/apply_job/',apply_job,name="apply_job"),
]
