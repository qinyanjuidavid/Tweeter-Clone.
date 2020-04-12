from django import forms
from django.forms import ModelForm
from tweeter.models import Tweet


class TweetCreationForm(ModelForm):
    class Meta:
        content=forms.CharField(label=" ",widget=forms.Textarea(
        attrs={'placeholder':"What's happening?","class":"form-control"}))
        model=Tweet
        fields=('content','image')
