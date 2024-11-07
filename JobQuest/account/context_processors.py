from .models import EmployerProfile

def add_user_type(request):
    is_company = False
    if request.user.is_authenticated:
        is_company = EmployerProfile.objects.filter(user=request.user).exists()
    
    return { 'is_company': is_company}
