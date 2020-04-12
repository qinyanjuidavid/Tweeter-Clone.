from django import forms
from django.forms import ModelForm
from tweeter.models import Tweet


class TweetCreationForm(ModelForm):
    class Meta:
        content=forms.CharField(widget=forms.Textarea,help_text="What's happening?")
        model=Tweet
        fields=('content','image')
