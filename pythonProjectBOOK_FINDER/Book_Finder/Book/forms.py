from django import forms
from Book.models import kitab

class kitabform(forms.ModelForm):
    class Meta:
        model = kitab
        fields = "__all__"
