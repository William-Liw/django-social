from django import forms
from .models import Dweet, Quote, Document

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
    # school_name = forms.CharField(max_length=255)
    # pdf_file = forms.FileF
    # ield()
    class Meta:
        model = Quote
        fields = "__all__"

class DocumentForm(forms.ModelForm):
    class Meta:
        model =Document
        fields = ('description', 'document',)