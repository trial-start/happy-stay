from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=20)
    description=models.CharField(max_length=30)
    rating=models.IntegerField()
    cost=models.CharField(max_length=20)
    city=models.CharField(max_length=20,default='')
    country=models.CharField(max_length=20,default='')
    about=models.CharField(max_length=500,default='')
class Explore(models.Model):
    name=models.CharField(max_length=20)
    description=models.CharField(max_length=100)
    rating=models.IntegerField()
    cost=models.CharField(max_length=20)
    city=models.CharField(max_length=20,default='')
    country=models.CharField(max_length=20,default='')
    about=models.CharField(max_length=500,default='')


class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    guests = models.PositiveIntegerField()
    card = models.CharField(max_length=16)
    expiry = models.CharField(max_length=7)
    cvv = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
