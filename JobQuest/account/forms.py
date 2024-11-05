from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,SetPasswordForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(label="Email Address")
    class meta:
        model = User
        field = ("username","email","password1","password2")
        
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'  # Adding Bootstrap class
            field.widget.attrs['placeholder'] = field.label 

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email') 
        if commit:
            user.save()
        return user

class CustomLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']
    
    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'  # Adding Bootstrap class
            field.widget.attrs['placeholder'] = field.label 

class PasswordChangeForm(SetPasswordForm):
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))



