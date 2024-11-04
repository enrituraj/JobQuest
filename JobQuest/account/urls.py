from django.urls import path
from .views import custom_login,change_password,logout_view,register_employer,register_seeker,profile,edit_profile
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('login/', custom_login, name="login"),
    path('logout/', logout_view, name='logout'),
    path('register/employer/', register_employer, name="register_employer"),
    path('register/seeker/', register_seeker, name="register_seeker"),
    path('profile/', profile, name="profile"),
    path('change_password/', change_password, name="change_password"),
    path('profile/edit/', edit_profile, name="edit_profile"),
]

