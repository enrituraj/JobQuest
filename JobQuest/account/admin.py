from django.contrib import admin
from .models import LoginHistory,EmployerProfile

# Register your models here.
@admin.register(LoginHistory)
class LoginHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'timestamp', 'ip_address', 'user_agent')
    search_fields = ('user__username', 'ip_address')

admin.site.register(EmployerProfile)