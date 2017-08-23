from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

from .models import Feedback
from .forms import FeedbackForm

@login_required
def user_private_page(request):
	# the page which only the page owner can view
	# and give out the messages for that particular user
	received_messages = Feedback.objects.filter(write_to = request.user)
	sent_messages = Feedback.objects.filter(written_by = request.user)
	return render(request, 'feedbacks/private_page.html', {'received_messages':received_messages, 'sent_messages':sent_messages})

@login_required
def received_messages(request, username):
	# get the user first
	user = get_object_or_404(User, username = username)
	# filter the content for the received messages for the above user
	received = Feedback.objects.filter(write_to = user)
	# display it
	return render(request, 'feedbacks/received.html', {'user':user, 'received':received})

@login_required
def sent_messages(request, username):
	# get the user first
	user = get_object_or_404(User, username = username)
	# filter the content for the sent messages for the above user
	sent = Feedback.objects.filter(written_by = user)
	# display it
	return render(request, 'feedbacks/sent.html', {'user':user, 'sent':sent})

@login_required
def send_message(request, username):
	# get that user based on the id
	user = get_object_or_404(User, username = username)
	# fill out the form based on submitted data
	if request.method == 'POST':
		form = FeedbackForm(data = request.POST)
		# check if it is valid or not
		if form.is_valid():
			# create a new message but don't send it yet
			new_message = form.save(commit = False)
			# send it to that particular user only
			new_message.written_by = request.user
			new_message.write_to = user
			# now save the message
			new_message.save()
			# redirect to some page
			return render(request, 'feedbacks/message_sent.html', {'new_message':new_message})

	else:
		form = FeedbackForm()

	return render(request, 'feedbacks/new_message.html', {'form':form})
