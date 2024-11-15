from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models  import User
from django.contrib.auth  import get_user_model

User = get_user_model() 

class SignUp(models.Model):
    USER_TYPE_CHOICES = [
        ('Patient', 'Patient'),
        ('Doctor', 'Doctor'),
        ('Admin', 'Admin'),
    ]
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    mobile_number = PhoneField(blank=True, help_text='Contact phone number')
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)

    def __str__(self):
        return self.email
    
class Appointment(models.Model):
    DEPT_CHOICES = [
        ('CARD', 'cardiology'),
        ('ENT', 'ent'),
        ('PED', 'dermatology'),
        ('ORTH', 'orthopedics'),
        ('NEUR', 'Neurology'),
        ('NEUR', 'Neurology'),
    ]
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    mobile_number = PhoneField(blank=True, help_text='Contact phone number')
    nic = models.CharField(max_length=20)  
    appointment_date = models.DateField()
    department_name = models.CharField(max_length=10, choices=DEPT_CHOICES)
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)