from django.contrib import admin

# Register your models here.
from .models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
	list_display = ['timestamp', 'write_to']
	list_filter = ['write_to']

admin.site.register(Feedback, FeedbackAdmin)