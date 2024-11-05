from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.utils import timezone
from .models import LoginHistory

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    ip_address = request.META.get('REMOTE_ADDR')
    user_agent = request.META.get('HTTP_USER_AGENT')
    
    # Create a new Login History
    LoginHistory.objects.create(
        user=user,
        timestamp=timezone.now(),
        ip_address=ip_address,
        user_agent=user_agent,
    )