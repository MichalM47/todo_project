from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile
from django.db.transaction import atomic


class UserCreationFormCustom(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        fields = ['first_name', 'last_name', 'username']

    nick = forms.CharField(label='Enter nickname', widget=forms.Textarea, min_length=2, max_length=10)
    biography = forms.CharField(label='Tell us your story with movies', widget=forms.Textarea, min_length=5)

    @atomic
    def save(self, commit=True):
        result = super().save(commit)
        nick = self.cleaned_data['nick']
        biography = self.cleaned_data['biography']
        profile = Profile(nick=nick, biography=biography, user=result)
        if commit:
            profile.save()
        return result
