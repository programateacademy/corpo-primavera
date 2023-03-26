from django import forms
from .models import Activities


class ActivitiesForm(forms.ModelForm):
    class Meta:
        model = Activities
        fields = '__all__'