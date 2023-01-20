from django.db import models

# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=255)
    featerd = models.BooleanField(default=False)
    order = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.TextField(null=True)
    description = models.TextField(null=True)
    image = models.ImageField()
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    Category = models.ForeignKey(Category, on_delete=models.PROTECT)


    def __str__(self):
        return self.name
