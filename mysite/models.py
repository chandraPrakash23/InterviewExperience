from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200,null=True)
    email = models.EmailField(unique=True,null=True)
    
