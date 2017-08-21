from django.conf.urls import url 


from . import views

urlpatterns = [
				url(r'^$', views.user_private_page, name = 'private_page'),
				# url to post a new message
				url(r'^message/(?P<username>[-\w]+)/$', views.send_message, name = 'send_message'),
				]