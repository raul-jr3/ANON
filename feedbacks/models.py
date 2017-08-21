from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Feedback(models.Model):
	write_to = models.ForeignKey(User, related_name = 'received')
	written_by = models.ForeignKey(User, related_name = 'written')
	reveal_identity = models.BooleanField(default = False)
	body = models.TextField(help_text = "say it out!")
	timestamp = models.DateTimeField(auto_now_add = True)
	make_public = models.BooleanField(default = False)

	def __str__(self):
		return "{}".format(self.timestamp)

	class Meta:
		ordering = ['-timestamp']