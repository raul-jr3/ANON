from django.conf.urls import url 


from . import views

urlpatterns = [
				url(r'^$', views.user_private_page, name = 'private_page'),
				# url to post a new message
				url(r'^message/(?P<username>[-\w]+)/$', views.send_message, name = 'send_message'),
				# received and sent messages
				url(r'^received/(?P<username>[-\w]+)/$', views.received_messages, name = 'received'),
				url(r'^(?P<username>[-\w]+)/sent/$', views.sent_messages, name = 'sent'),
				]