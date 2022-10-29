from django.db import models
from django.contrib.auth.models import BaseUserManager ,AbstractBaseUser

# Create your models here.

class AccountManager(BaseUserManager):
    def create_user(self,name,email,password=None,is_staff=False):
        if not email:
            raise ValueError('must provide an email')

        
        user=self.model(
            email       =  self.normalize_email(email),
            name        =  name,
            
        )

        user.set_password(password)
        user.save(using=self._db)
        return user 
    
    def create_superuser(self,email,name,password):
        user = self.create_user(
            email       =  self.normalize_email(email),
            name        =  name,
            password     = password,
        )
        user.is_admin        = True
        user.is_active       = True
        user.is_staff        = True
        user.is_superadmin   = True
        user.save(using=self._db)   
        return user

class Account(AbstractBaseUser):
    email           =models.EmailField(max_length=100,unique=True) 
    name            =models.CharField(max_length=50)
    is_admin        =models.BooleanField(default=False)
    is_staff        =models.BooleanField(default=False)
    is_active       =models.BooleanField(default=True)
    is_verified     =models.BooleanField(default=False)
    is_superadmin   =models.BooleanField(default=False)

    USERNAME_FIELD  ='email'
    REQUIRED_FIELDS =['name']
    
    objects=AccountManager()

    

    def __str__(self):
        return self.email
    
    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    def has_module_perms(self,add_label):
        return True