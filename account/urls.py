from django.conf.urls import url 

from django.contrib.auth import views as auth_views


urlpatterns = [
				# login and logout
				url(r'^login/$', auth_views.login, name = 'login'),
				url(r'^logout/$', auth_views.logout, name = 'logout'),
				]