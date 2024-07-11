from django.db import models

class Category(models.Model):
    slug=models.CharField(max_length=50,null=False,blank=False)
    name=models.CharField(max_length=50,null=False,blank=False)
    image=models.ImageField(upload_to="img",null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0=default,1=Hidden")
    trending=models.BooleanField(default=False,help_text="0=default,1=Hidden")

    def __str__(self):
        return self.name


class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    slug = models.CharField(max_length=100, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    proimage=models.ImageField(upload_to="img",null=False,blank=False)
    description=models.CharField(max_length=500, null=False, blank=False)
    quantity=models.IntegerField(null=False,blank=False)
    original_price=models.FloatField(null=False,blank=False)
    selling_price=models.FloatField(null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0=default,1=Hidden")
    trending = models.BooleanField(default=False, help_text="0=default,1=Hidden")

    def __str__(self):
        return self.name



