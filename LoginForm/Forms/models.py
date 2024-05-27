from django.db import models

class Studentform(models.Model):
    name=models.CharField(max_length=255)
    f_name=models.CharField(max_length=255)
    m_name=models.CharField(max_length=255)
    dob=models.DateField()
    #gender=models.BooleanField()
    address=models.CharField(max_length=255)
    email=models.EmailField()
    m_no=models.CharField(max_length=255)
    
