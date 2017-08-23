from django.db import models
from django.conf import settings
# Create your models here.


class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name = 'profile')
	display_picture = models.ImageField(upload_to = '%Y/%m/%d/profile_pictures/', blank = True)


	def __str__(self):
		return "{}".format(self.user)