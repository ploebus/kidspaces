from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Trees(models.Model):
    tree_name = models.CharField(max_length=30)
    tree_type = models.CharField(max_length=30)
    tree_description = models.CharField(max_length=255)
    lat = models.CharField(max_length=17)
    lng = models.CharField(max_length=17)
    first_branch_height = models.IntegerField(max_length=255,blank=True)
    heighest_reach = models.IntegerField(max_length=255,blank=True)
    drop_zone = models.IntegerField(max_length=255,blank=True)
    date_created = models.DateTimeField(auto_now_add=True,blank=True)
    age_range = models.CharField(max_length=30,blank=True)
    accessibility=models.IntegerField(blank=True)
    tree_fruit = models.BooleanField(blank=True)
    tree_view = models.BooleanField(blank=True)
    tree_animals = models.BooleanField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='+')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tree_name

class Ratings(models.Model):
    message = models.TextField(max_length=300)
    photo_link = models.CharField(max_length=50)
    rating_overall = models.IntegerField()
    rating_climbability = models.IntegerField()
    rating_interest = models.IntegerField()
    rating = models.ForeignKey(Trees, on_delete=models.CASCADE,related_name='ratings')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='+')	


