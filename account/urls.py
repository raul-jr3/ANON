from django.conf.urls import url 
from django.core.urlresolvers import reverse

from django.contrib.auth import views as auth_views


from . import views

urlpatterns = [
				# login and logout
				url(r'^login/$', auth_views.login, name = 'login'),
				url(r'^logout/$', auth_views.logout, name = 'logout'),
				# register 
				url(r'^register/$', views.register, name = 'register'),
				# change password
				url(r'^change-password/$', auth_views.PasswordChangeView.as_view(success_url = 'done/'), name = 'password_change'),
				url(r'^change-password/done/$', auth_views.PasswordChangeDoneView.as_view(), name = 'password_change_done'),
				# account and profile settings
				url(r'^settings/(?P<username>[-\w]+)/$', views.account_settings, name = 'settings'),
				]