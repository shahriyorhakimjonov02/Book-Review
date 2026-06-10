from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth.models import User
from src.core.models import Book, Category
from django import forms

from django.forms.widgets import PasswordInput, TextInput

class CreateUserForm(UserCreationForm):

     class Meta:
         model = User
         fields = ('username', 'first_name', 'last_name' ,'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields= '__all__'
