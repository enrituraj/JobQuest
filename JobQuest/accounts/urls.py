from django.urls import path
from .views import login,logout,register_employer,register_seeker,profile,edit_profile

urlpatterns = [
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('register/employer/', register_employer, name="register_employer"),
    path('register/seeker/', register_seeker, name="register_seeker"),
    path('profile/', profile, name="profile"),
    path('profile/edit/', edit_profile, name="edit_profile"),
]

