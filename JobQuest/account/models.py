from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class LoginHistory(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.user.username} logged in at {self.timestamp}"
    
class EmployerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    company_website = models.URLField(max_length=255)

    def __str__(self) -> str:
        return f"{self.user.username} - {self.company_name}"
    
    