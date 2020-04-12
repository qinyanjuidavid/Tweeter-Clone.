from django.db import models
from accounts.models import User
from tweeter.validators import validate_content

class Tweet(models.Model):
    content=models.TextField(max_length=500,validators=[validate_content])
    updated=models.DateTimeField(auto_now=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to="mypicts",blank=True,null=True)


    def __str__(self):
        return self.user.username
