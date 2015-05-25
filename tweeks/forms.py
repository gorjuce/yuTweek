from django.forms import ModelForm
from tweeks.models import Tweek

class TweekForm(ModelForm):
    class Meta:
        model = Tweek
        fields = ['content']