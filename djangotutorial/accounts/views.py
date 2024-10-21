from django.contrib.auth import login, logout as auth_logout
from django.shortcuts import redirect, render
from django.db.utils import IntegrityError
from .forms import RegistrationForm


def sign_up(request):

    # if the page is making a POST
    if request.method == "POST":
        # create a form with the submitted POST data
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # the RegistrationForm inherits from the Django UserCreateForm which returns a user if the form is valid
            try:
                user = form.save()

                # login the new user and redirect to the landing page
                login(request, user)
                return redirect("/")
            except IntegrityError:
                # if the form.save() function fails due to database integrity, set the error to be displayed in the form on the template
                form.errors["email"] = ['User with this email is already registered']

    else:
        # load a form for a GET request for the user to fill out
        form = RegistrationForm()

    return render(request, "register.html", {"form": form})

def logout(request):
    # utilize Django's built in auth_logout function for the session, found in the request and redirect to the landing page
    auth_logout(request)
    return redirect("/")