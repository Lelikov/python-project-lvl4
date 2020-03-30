from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.RegexField(max_length=150,
                                regex=r'^[\w.@+-]+$',
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control mb-1',
                                           'placeholder': 'Username',
                                           'maxlength': '150', 'required': True,
                                           'autofocus': True
                                           }),
                                error_messages={'invalid': 'Enter a valid name'})
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control mb-2',
               'placeholder': 'Email',
               'required': True,
               }))

    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control mb-1',
               'placeholder': 'Password',
               'minlength': '8',
               'required': True, }))

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control mb-2',
               'placeholder': 'Confirm password',
               'minlength': '8',
               'required': True, }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        user = self.get_user()
        if not user or not user.is_active:
            raise forms.ValidationError('Invalid login or password')
        return self.cleaned_data

    def get_user(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user
