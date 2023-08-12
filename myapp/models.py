from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Box(models.Model):
    img = models.CharField(max_length=100)
    class Meta:
        abstract=True



class SmallImages(Box):
    label = models.CharField(max_length=100)
    def __str__(self):
        return self.label
    
class ShoeColor(Box):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ShoeSize(models.Model):
    size = models.CharField(max_length=10)

    def __str__(self):
        return self.size

class MainImage(Box):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    small_images = models.ManyToManyField(SmallImages, blank=True)
    colors = models.ManyToManyField('ShoeColor')
    sizes = models.ManyToManyField('ShoeSize')

    @property
    def get_small_images(self):
        return self.small_images.all()
    
    @property
    def get_color(self):
        return self.colors.all()
    
    @property
    def get_size(self):
        return self.sizes.all()
    
    
    
    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(MainImage, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    size = models.ForeignKey(ShoeSize, on_delete=models.SET_NULL, null=True, blank=True)
    color = models.ForeignKey(ShoeColor, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} size {self.size} {self.color}  {self.product.name} added by {self.user.username}"