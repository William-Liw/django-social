from django import forms
from .models import Dweet, Quote

class DweetForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Dweet something...",
                "class": "textarea is-success is-medium",
            }
        ),
        label ="",
    )

    class Meta:
        model = Dweet
        exclude = ("user", )

class QuoteForm(forms.ModelForm):

    class Meta:
        model = Quote
        fields = "__all__"
