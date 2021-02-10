from django import forms
from .models import Comments, Post, Music

class NewPostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['description', 'pic', 'tags']
		widgets = {
          'description': forms.Textarea(attrs={'rows':3, 'cols':15}),
        }




class NewCommentForm(forms.ModelForm):

	class Meta:
		model = Comments
		fields = ['comment']


class MusicForm(forms.ModelForm):
	class Meta:
		model = Music
		fields = ['track', 'title', 'artwork']
		widgets = {
          'title': forms.Textarea(attrs={'rows':1, 'cols':1}),
        }

