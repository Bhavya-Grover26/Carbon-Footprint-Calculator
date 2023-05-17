from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name

class Calculate(models.Model):
    CATEGORY = (
        ('Individual', 'Individual'),
        ('Organisation', 'Organisation'),
    )
    user = models.ForeignKey(User,null=True, on_delete=models.SET_NULL)
    choice = models.CharField(max_length=200,null=True,choices=CATEGORY)
    
    def _str_(self):
        return self.user

class Individual(models.Model):
    CATEGORY = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('Dont use', 'Dont use'),
    )
    calculate = models.ForeignKey(Calculate,null=True, on_delete=models.SET_NULL)
    gas = models.FloatField(null=True)
    electricity = models.FloatField(null=True)
    flightsless= models.FloatField(null=True)
    flightsmore= models.FloatField(null=True)
    newspaper = models.CharField(max_length=200,null=True,choices=CATEGORY)
    aluminium = models.CharField(max_length=200,null=True,choices=CATEGORY)

class Organisation(models.Model):
    CATEGORY = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('Dont use', 'Dont use'),
    )
    calculate = models.ForeignKey(Calculate,null=True, on_delete=models.SET_NULL)
    distance = models.FloatField(null=True)
    electricity = models.FloatField(null=True)
    flightsless= models.FloatField(null=True)
    flightsmore= models.FloatField(null=True)
    newspaper = models.CharField(max_length=200,null=True,choices=CATEGORY)
    ghg = models.CharField(max_length=200,null=True,choices=CATEGORY)





    
    