from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Poll, Choice

def index(request):
	all_polls = Poll.objects.all()
	context = {'all_polls':all_polls}
	return render(request, 'polls/index.html', context)

def detail(request, poll_id):
	poll = Poll.objects.get(id=poll_id)
	poll_question = poll.question
	poll_choices = poll.choice_set.all()
	context = {'poll_choices':poll_choices, 'poll_id':poll.id}
	return render(request, 'polls/detail.html', context)

def vote(request, poll_id, vote_choice):
	poll = Poll.objects.get(id=poll_id)
	choice_voted = poll.choice_set.get(id=vote_choice)
	choice_voted.votes += 1
	choice_voted.save()
	return HttpResponse("your vote for poll %s has been recorded succesfully." % poll_id)

def results(request, poll_id):
	poll = Poll.objects.get(id=poll_id)
	context = {'question':poll.question, 'vote_standings':poll.choice_set.values()}
	return render(request, 'polls/results.html', context)
