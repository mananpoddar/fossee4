from django.db import models
from django import forms
from fossee4.models import Images

class inputImages(forms.ModelForm):
    class Meta:
        model = Images
        fields= '__all__'