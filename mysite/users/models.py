from django.db import models
from django.contrib.auth.models import User    # inbuilt model

# Create your models here.
class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE) # means on deleting user it needs to del profile also
    
    # whenever using image field we need to install pillow
    image= models.ImageField(default='profilepic.jpg', upload_to='profile_pictures')
    
    location = models.CharField(max_length=100)

    # string representation wheneber we try to access obj use should get username
    def __str__(self):
        return self.user.username