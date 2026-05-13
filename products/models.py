from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    

    def __str__(self):
        return f"category is {self.name}"
    
class Products(models.Model):
    name = models.CharField()
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.FloatField(default = 1)
    image = models.ImageField(upload_to='static/images')
    created_at = models.DateTimeField(auto_now_add=True)
    is_available = models.BooleanField(default = True)

    def __str__(self):
        return f"product {self.name}"

