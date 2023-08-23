from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import authentification_users
from .form import SignupForm  # Renamed form.py to forms.py

# View for user registration
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # Save the user's registration data from the form
            form.save()

            # Determine user's plan and set allowed login attempts
            plan = request.POST['plan']
            if plan == "Normal":
                allowed_login_attempts = 5
            elif plan == "Medium":
                allowed_login_attempts = 7
            else:
                allowed_login_attempts = 10

            # Create a new user instance and save it
            new_user = authentification_users(
                username=request.POST['username'],
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST['email'],
                plan=allowed_login_attempts,
            )
            new_user.save()

            return redirect('login')  # Redirect to the login page
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})

# View for user login
def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)  # Authenticate and log in the user
            return redirect('next')  # Redirect to the next page after successful login
        else:
            error_message = "Invalid username or password. Please try again."
    else:
        error_message = ""

    return render(request, 'login.html', {'error_message': error_message})

# View for the next page (destination after successful login)
def next_page(request):
    return render(request, 'next.html')
