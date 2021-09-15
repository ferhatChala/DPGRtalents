from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from app.models import Travaille,These
#user costum configiration

class MyUserManager(BaseUserManager):
    def create_user(self,email,username,password=None):
        if not email:
            raise ValueError('users must have an email adress')
        if not username:
            raise ValueError('users must have userame)')
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )

        user.set_password(password)
        user.save(using = self._db)
        return user
    def create_superuser(self,email,username,password):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
            username = username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    
class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="email",max_length=60,unique=True)
    username = models.CharField(max_length=30,unique=True)
    date_joined = models.DateTimeField(verbose_name="date_joined",auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login",auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_doctorant = models.BooleanField(default=False)
    is_these_dir = models.BooleanField(default=False)
    is_dpgr = models.BooleanField(default=False)
    is_cfd = models.BooleanField(default=False)
    is_lab_dir = models.BooleanField(default=False)
    is_cs = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = MyUserManager()

    def __str__(self):
        return self.email
    
    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    def has_module_perms(self,app_label):
        return True


#les utulisateurs de la DPGR

class Doctorant(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE, primary_key = True)
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    phone= models.CharField(max_length=20)
    Adress = models.CharField(max_length=50)
    date_naissance = models.DateTimeField(verbose_name="date_joined")
    #volet acadimique
    univ_origin = models.CharField(max_length=20)
    these = models.ForeignKey('app.These',related_name='theses',on_delete=models.CASCADE)
    anne_univ = models.IntegerField()
    master_D = models.CharField(max_length=20)
    dir_these = models.ForeignKey('DThese',related_name='theses',on_delete=models.CASCADE)


    def __str__(self):
        return self.nom 

class Teacher(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE, primary_key = True)
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    phone= models.CharField(max_length=20)
    Adress = models.CharField(max_length=50)
    date_naissance = models.DateTimeField(verbose_name="date_joined",auto_now_add=False)
    grade = models.ForeignKey('Grade',related_name='Gteachers',on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class DPGRuser(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE, primary_key = True)
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    phone= models.CharField(max_length=20)
    Adress = models.CharField(max_length=50)
    date_naissance = models.DateTimeField(verbose_name="date_joined",auto_now_add=False)
    grade = models.ForeignKey('Grade',related_name='Gdpgrs',on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class DThese(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE, primary_key = True)
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    phone= models.CharField(max_length=20)
    Adress = models.CharField(max_length=50)
    date_naissance = models.DateTimeField(verbose_name="date_joined",auto_now_add=False)
    grade = models.ForeignKey('Grade',related_name='GDTheses',on_delete=models.CASCADE)

    def __str__(self):
        return  self.nom

class DLab(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE, primary_key = True)
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    phone= models.CharField(max_length=20)
    Adress = models.CharField(max_length=50)
    date_naissance = models.DateTimeField(verbose_name="date_joined",auto_now_add=False)
    grade = models.ForeignKey('Grade',related_name='GDLabs',on_delete=models.CASCADE)

    def __str__(self):
        return  self.nom

class CFDuser(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE, primary_key = True)
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    phone= models.CharField(max_length=20)
    Adress = models.CharField(max_length=50)
    date_naissance = models.DateTimeField(verbose_name="date_joined",auto_now_add=False)
    grade = models.ForeignKey('Grade',related_name='GCFDusers',on_delete=models.CASCADE)

    def __str__(self):
        return  self.nom

class CSuser(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE, primary_key = True)
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    phone= models.CharField(max_length=20)
    Adress = models.CharField(max_length=50)
    date_naissance = models.DateTimeField(verbose_name="date_joined",auto_now_add=False)
    grade = models.ForeignKey('Grade',related_name='GCSusers',on_delete=models.CASCADE)

    def __str__(self):
        return  self.nom



class Grade(models.Model):
    nom = models.CharField(max_length=50)
    Discription = models.CharField(max_length=50)
    
    def __str__(self):
        return  self.nom
