from django import forms
from .models import Comments, Post, Music, Video
from crispy_forms.bootstrap import InlineField
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from crispy_forms.helper import FormHelper


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
		fields = ['title', 'artist_name', 'track', 'artwork']
		widgets = {
          'title': forms.Textarea(attrs={'rows':1, 'cols':1}),
		  'artist_name': forms.Textarea(attrs={'rows':1, 'cols':1}),
        }



class VideoForm(forms.ModelForm):
	class Meta:
		model = Video
		fields = ['video']
		
