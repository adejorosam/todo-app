from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name #name to be shown when called


class Task(models.Model):
    title = models.CharField(max_length=250, blank=True)
    description = models.CharField(max_length=200)
    created = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
    due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date 
    category = models.ForeignKey(Category, default="general", on_delete = models.CASCADE)

    
    def __str__(self):
        return self.title #name to be shown when called

    

