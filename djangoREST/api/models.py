from django.db import models

# Create your models here.


# Creating company midel 
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    location = models.CharField(max_length=40)
    about = models.TextField()
    type = models.CharField(max_length=100 ,choices=
    (('IT','it'),
    ('Non it', 'non it'), 
    ('mobile phones', 'mobile phones')
    ))
    added_date= models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    
    def __str__(self):
        return self.name +" "+ self.location


#Employee model
class Employee(models.Model):
    name=models.CharField(max_length=20)
    email= models.CharField(max_length=20)
    address= models.CharField(max_length=40)
    phone=models.CharField(max_length=30)
    about=models.TextField(max_length=100)
    position=models.CharField(max_length=50 ,choices=(
        ('manager','manager'),
        ('developer','developer'),
        ('hr','hr')
    ))
    company = models.ForeignKey(Company,on_delete=models.CASCADE)



