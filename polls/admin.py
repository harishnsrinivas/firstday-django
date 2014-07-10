from django.contrib import admin
from polls.models import Poll, Choice

class ChoiceInline(admin.StackedInline):
	model = Choice
	extra = 0

class PollAdmin(admin.ModelAdmin):
	fieldsets=[
		(None, {'fields':['question']}),
		('Date Info', {'fields':['pub_date']})]

	inlines = [ChoiceInline]

admin.site.register(Poll, PollAdmin)

