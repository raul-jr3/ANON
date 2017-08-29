from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

from .forms import RegisterForm, ProfileEditForm, UserEditForm
from .models import Profile

def register(request):
	# check the request method
	if request.method == 'POST':
		# accept the user data
		form = RegisterForm(data = request.POST)
		# check if the data is valid
		if form.is_valid():
			# create a new user
			new_user = form.save(commit = False)
			# assign the password
			new_user.set_password(form.cleaned_data['password'])
			# save the user
			new_user.save()
			# create a new profile for that user
			profile = Profile.objects.create(user = new_user)
			# display success message
			return render(request, 'registration/register_success.html', {'new_user':new_user})

	else:
		# give out a blank form
		form = RegisterForm()
	return render(request, 'registration/register.html', {'form':form})

@login_required
def account_settings(request, username):
	# get the user from the database
	user = get_object_or_404(User, username = username)
	if request.method == 'POST':
		form = ProfileEditForm(data = request.POST, instance = user.profile, files = request.FILES)
		user_form = UserEditForm(data = request.POST, instance = user)
		if form.is_valid() and user_form.is_valid():
			# save the updated information
			form.save()
			user_form.save()
			#redirect to that page itself
			messages.success(request, "Profile updated successfully")
	else:
		form = ProfileEditForm(instance = user.profile)
		user_form = UserEditForm(instance = user)
	# give out the page and links to edit
	return render(request, 'account/settings.html', {'user':user, 'form':form, 'user_form':user_form})

