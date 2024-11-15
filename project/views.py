from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib import messages

User = get_user_model()

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import SignUp
# from .forms import SignUpForm  # You can create a form class for better form validation

def signup(request):
    if request.method == "POST":
        # Retrieve form data
        user_type = request.POST.get('user_type')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        mobile_number = request.POST.get('mobile_number')
        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Validate that the passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('/signup/')

        # Check if the email is already in use
        if SignUp.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('/signup/')

        # Create new user (using the SignUp model)
        signup_user = SignUp(
            user_type=user_type,
            first_name=first_name,
            last_name=last_name,
            email=email,
            mobile_number=mobile_number,
            date_of_birth=date_of_birth,
            gender=gender,
            password=password,
            confirm_password=confirm_password
        )

        # Save user to the database
        signup_user.save()

        # Optionally, create a user in the built-in User model as well
        # user = User.objects.create_user(
        #     username=email,  # Use email as the username
        #     first_name=first_name,
        #     last_name=last_name,
        #     email=email
        # )

        # Set the password
        # user.set_password(password)
        # user.save()

        # Show success message and redirect
        messages.success(request, "Account created successfully!")
        # return redirect('/login/')  # Redirect to login page after successful signup

    return render(request, 'signup.html')

def aboutus(request):
    return render(request,"aboutus.html")

def home(request):
    return render(request,"home.html")