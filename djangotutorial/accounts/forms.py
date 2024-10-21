from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["email", "password1", "password2"]

    def save(self, commit=True):

        # create the user object, but don't commit to the database yet, we need to set the username field for our implementation
        user = super().save(commit=False)

        # overriding the base form, set the django username field of the email address captured in the sign up form
        username = self.cleaned_data["email"]
        user.username = username

        # now save the user to the database (commit=True is the default)
        return super().save()
