from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self,email,password,**extra_fields):
        if(not email):
            raise ValueError(('The Email must be set'))
        email=self.normalize_email(email)
        user=self.model(email=email,**extra_fields)
        extra_fields.setdefault('profile_picture',"default/static")
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_verified', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

#custom user model
class User(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(max_length=255,unique=True)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    profile_picture=models.ImageField(blank=True,upload_to='profiles',default="default.jpg")
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_verified=models.BooleanField(default=False)
    is_doctor=models.BooleanField(default=False)
    objects=UserManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name','is_verified','profile_picture']

    def get_full_name(self):
        return self.first_name+" "+self.last_name
    def get_short_name(self):
        return self.first_name
    def __str__(self):
        return self.email

class Hospital(models.Model):
    name=models.TextField(max_length=255)
    address=models.TextField(max_length=500)
    rating=models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    def __str__(self):
        return str(self.name)
    
class DoctorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_profile')
    degree=models.FileField(upload_to='degree')
    specialization=models.TextField(max_length=255)
    hospital=models.ForeignKey(Hospital,on_delete=models.CASCADE,default=None)
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}'s Doctor Profile"

class Report(models.Model):
    patient=models.ForeignKey(User,on_delete=models.CASCADE);
    symptoms=models.TextField(max_length=255);
    address=models.TextField(max_length=255);
    def __str__(self):
        return str(self.patient.first_name)
