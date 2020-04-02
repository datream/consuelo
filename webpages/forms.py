from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class CustomUserForm(forms.Form):
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2


class CustomUserCreationForm(CustomUserForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "id": "username", "placeholder": "Username"}),
        label='Enter Username', min_length=4, max_length=150)
    email = forms.CharField(
        widget=forms.EmailInput(attrs={"class": "form-control", "id": "email", "placeholder": "Email"}),
        label="Enter Email")
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "id": "password1", "placeholder": "Password"}),
        label="Enter Password")
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "id": "password2", "placeholder": "Password"}),
        label="Confirm Password")

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("Username already exists")
        return username

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user


class CustomUserUpdationForm(CustomUserForm):
    user = User.objects.get(pk=1)
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "id": "first_name",
                                      "placeholder": "First Name" if user.first_name is "" else user.first_name}),
        label='Change First Name:', min_length=4, max_length=150, required=False)
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", "id": "last_name",
                                      "placeholder": "Last Name" if user.last_name is "" else user.last_name}),
        label='Change Last Name:', min_length=4, max_length=150, required=False)
    email = forms.CharField(
        widget=forms.EmailInput(attrs={"class": "form-control", "id": "email",
                                       "placeholder": "Email" if user.email is "" else user.email}),
        label="Change Email", required=False)
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "id": "password1", "placeholder": "Password"}),
        label="Change Password", required=False)
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "id": "password2", "placeholder": "Password"}),
        label="Confirm Password", required=False)

    def save(self, username, commit=True):
        user = username
        print("*********** User:", user, end="***********\n")

        if self.cleaned_data['email'] is not "":
            user.email = self.cleaned_data['email']

        if self.cleaned_data['first_name'] is not "":
            user.first_name = self.cleaned_data['first_name']

        if self.cleaned_data['last_name'] is not "":
            user.last_name = self.cleaned_data['last_name']

        if self.cleaned_data['password1'] != "" and self.cleaned_data['password2'] != "":
            user.set_password(self.cleaned_data['password1'])

        user.save()
