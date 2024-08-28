from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=255, default="name")
    ingredients = models.TextField()
    description = models.TextField()
    image =models.ImageField(upload_to='images/')
    posted_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name