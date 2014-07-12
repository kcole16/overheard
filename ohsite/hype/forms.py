from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.forms import UserCreationForm

from datetime import datetime

from core.models import Account, AccountManager
from hype.models import HypeComment

class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(CommentForm, self).__init__(*args, **kwargs)

    class Meta:
        model = HypeComment
