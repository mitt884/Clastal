from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from .models import User

class ChangeUserPassword(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}), label='Password')
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}), label='Confirm Password')
    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']

class UserUpdateForm(UserChangeForm):
    username = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control form-control-lg'}))
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control form-control-lg'}))
    university = forms.ChoiceField(choices=User.UNIVERSITY_CHOICES, widget=forms.Select(attrs={'class': 'form-control form-control-lg'}))
    is_creator = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), label='Is Creator')

    class Meta:
        model = User
        fields = ['username', 'age', 'email', 'university', 'is_creator']

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control form-control-lg'}))
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control form-control-lg'}))
    university = forms.ChoiceField(choices=User.UNIVERSITY_CHOICES, widget=forms.Select(attrs={'class': 'form-control form-control-lg'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}), label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'}), label='Confirm Password')
    is_creator = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), label='Is Creator')

    class Meta:
        model = User
        fields = ['username', 'age', 'email', 'university', 'password1', 'password2', 'is_creator']
