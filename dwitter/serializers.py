from .models import Quote
from rest_framework.serializers import ModelSerializer

class CreateQuoteSerializer(ModelSerializer):
    class Meta:
        model = Quote
        exclude = ("user", "invoice_no", "pdf_file")

class QuoteSerializer(ModelSerializer):
    class Meta:
        model = Quote
        fields = "__all__"