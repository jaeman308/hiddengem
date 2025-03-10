from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.


class HiddenGem(models.Model):
    title =models.CharField(max_length=50)
    class Category(models.TextChoices):
        FOOD = 'Food', 'Food'
        DRINK = 'Drink', 'Drink'
        PARK = 'Park', 'Park'
        ART = 'Art', 'Art'
        ATTRACTIONS = 'Attractions', 'Attractions'
        NIGHTLIFE = 'Nightlife', 'Nightlife'
        MUSIC = 'Music', 'Music'
        THEATRE = 'Theatre', 'Theatre'
        MUSEUMS = 'Museums', 'Museums'

    category = models.CharField(
        max_length=255,
        choices=Category.choices,
        default=Category.FOOD,
    )
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('hiddengem-detail', kwargs={'hiddengem_id': self.id})


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    hiddengem = models.ForeignKey(HiddenGem, on_delete=models.CASCADE)
    comment = models.TextField(max_length=255) 

    def __str__(self):
        return self.comment
    
    def get_absolute_url(self):
        return reverse('hiddengem-detail', kwargs={'hiddengem_id': self.hiddengem.id})


class Activity(models.Model):
    comment = models.ForeignKey('Comment', on_delete=models.CASCADE, null=True, blank=True)
    like = models.IntegerField(default=0)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hiddengem = models.ForeignKey(HiddenGem, on_delete=models.CASCADE)

    def __str__(self):
        return f"Activity by {self.user.username} on {self.hiddengem.title}"

