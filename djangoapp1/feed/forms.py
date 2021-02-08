from django import forms
from .models import Comments, Post

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

