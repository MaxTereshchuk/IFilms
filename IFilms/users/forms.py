from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from users.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'name': "username", 'placeholder': "Enter your username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'name': "password", 'placeholder': "Enter your password"}))

    class Meta:
        model = User
        fields = ('username', 'password')

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'name': "username", 'placeholder': "Enter your username"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'name': "email", 'placeholder': "Enter your email"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'name': "password1", 'placeholder': "Create a password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'name': "password2", 'placeholder': "Confirm your password"}))

    class Meta:
        model = User
        fields = {'username', 'email', 'password1', 'password2'}

class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'first-name', 'placeholder': "First Name"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'second-name', 'placeholder': "Second Name"}))
    country = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'country', 'placeholder': "Country"}))
    favourite_movie = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'fav-movie', 'placeholder': "Favourite movie"}))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'username', 'placeholder': "Username", 'readonly': True}))
    email = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'email', 'placeholder': "E-mail", 'readonly': True}))


    class Meta:
        model = User
        fields = {'first_name', 'last_name', 'country', 'favourite_movie', 'username', 'email'}