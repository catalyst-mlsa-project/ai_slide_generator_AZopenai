from django import forms
from .models import PowerPointTemplate

class SlideGenerationForm(forms.Form):
    prompt = forms.CharField(max_length=200, required=True)
    template = forms.ModelChoiceField(queryset=PowerPointTemplate.objects.all(), required=False, empty_label="Select a Template")
    custom_template = forms.FileField(required=False)  # For custom file upload


    
