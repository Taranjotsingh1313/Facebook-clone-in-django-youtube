from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class profilemodel(models.Model):
    image = models.ImageField(upload_to="ProfilePics")
    bio = models.CharField(max_length=200)
    followers = models.ManyToManyField(User,related_name='followers',blank=True,null=True)
    following  = models.ManyToManyField(User,blank=True,null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="user")

class Post(models.Model):
    post = models.ImageField(upload_to="posts")
    profileuser = models.ForeignKey(profilemodel,related_name="profile",on_delete=models.CASCADE)
    likes = models.ManyToManyField(User,related_name="likes",blank=True,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

