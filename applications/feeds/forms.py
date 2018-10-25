from django import forms
from .models import Comments, AnsweraQuestion, AskaQuestion
from pagedown.widgets import PagedownWidget

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comments
		fields = ('comment_text',)

class AnswerForm(forms.ModelForm):
	content = forms.CharField(widget=PagedownWidget(show_preview=False))
	class Meta:
		model = AnsweraQuestion
		fields = [
			'content'
		]

class QuestionForm(forms.ModelForm):
	description = forms.CharField(widget=PagedownWidget(show_preview=False))
	class Meta:
		model = AskaQuestion
		fields = [
			'description',
		]