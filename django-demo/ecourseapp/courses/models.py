from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class BaseModel(models.Model):
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    class Meta:
        abstract = True

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Course(BaseModel):
    subject = models.CharField(max_length=100)
    description = models.CharField(max_length=25)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE)
    image = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.subject
