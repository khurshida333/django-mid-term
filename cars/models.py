from django.db import models
from brands.models import Brand
from django.contrib.auth.models import User
# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,unique=True,null=True,blank=True) #slug
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  #ex: 20000.00
    content = models.TextField(default='There is no Description for this car.')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, default='Unknown')  # Link to Brand model
    quantity = models.PositiveIntegerField(default=1)  # Add quantity field
    buyers = models.ManyToManyField(User, related_name='purchased_cars', blank=True)
    image = models.ImageField(upload_to='car_posts/media/uploads/', blank = True, null = True)
    def __str__(self):
        return  self.name       #str er use ki ? eta ekhane ken? bujhi nai
    

class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models. DateTimeField(auto_now_add=True) # jkhn e ei class er object toiri

    def _str_(self):
       return f"Comments by {self.name}"