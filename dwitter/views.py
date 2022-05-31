# from cv2 import log
import io


from django.shortcuts import render, redirect
from .forms import DweetForm, QuoteForm
from .models import Profile, Dweet, Quote
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.http import FileResponse
from django.conf import settings
from rest_framework.generics import ListCreateAPIView
from .serializers import QuoteSerializer, CreateQuoteSerializer
from drf_yasg.utils import swagger_auto_schema
from django.core.files import File
from django.template.loader import get_template
from weasyprint import HTML
from django.core.files.base import ContentFile


default_val = {
    "school_name" : "willschool",
    "to_email" : "email@thelessonspace.com",
    "school_size" : 1,
    "price_per_student" : 250,
    "total" : 250,
    "currency" : "ZAR",
    "to_name" : "recipient",
    "date" : "2022-05-11",
    "school_address" : "school address",
    "school_country" : "South Africa",
    "special_comments" : "special comments",
    "discount" : 0,
    "bank_detail" : """Bank: First National Bank (FNB)
                Name: SkillUp Tutors
                Branch Code: 250655
                Account Number: 62530958018
                SWIFT Code: FIRNZAJJ`,"""

}

@login_required
def dashboard(request):
    form = DweetForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            return redirect("dwitter:dashboard")

    followed_dweets = Dweet.objects.filter(
        user__profile__in=request.user.profile.follows.all()
    ).order_by("-created_at")
    return render(
        request,
        "dwitter/dashboard.html",
        {"form": form, "dweets": followed_dweets},
        )

# @login_required
# class DashboardView():
#     form = DweetForm
#     def post(self, request, *args, **kwargs):

#         return redirect("dwitter:dashboard")

@login_required
def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "dwitter/profile_list.html", {"profiles": profiles})

@login_required
def profile(request, pk):
    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()

    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get('follow')
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    return render(request, "dwitter/profile.html", {"profile": profile})

class LoginForm(AuthenticationForm):
    template_name = "dwitter/dashboard.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('members:members-home')
        return super('dwitter:dashboard', self).dispatch(request, *args, **kwargs)
  
def upload_file(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST, request.FILES)
        if form.is_valid():
            quote = form.save(commit=False)
            quote.user = request.user
            quote.save()
            return redirect("dwitter:upload_file")
    else:
        form = QuoteForm(request.FILES)
    return render(request, 'upload.html', {"form": form})

class QuoteView(ListCreateAPIView):
    _type = "Proforma Invoice"
    serializer_class = QuoteSerializer
    queryset = Quote.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return QuoteSerializer
        else:
            return CreateQuoteSerializer


    def createPdf(self, data):  
        raw_html = get_template("invoices/quote.html").render({"title": self._type, **data})
        doc = HTML(string=raw_html)
        pdf = io.BytesIO()
        doc.write_pdf(target=pdf)
        pdf.seek(0)
        pdf.html = raw_html
        return pdf

    @swagger_auto_schema(auto_schema=None)
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        data["currency"] = CURRENCY_MAP[data["currency"]]
        data["total"] = data["price_per_student"] * data["school_size"]
        data["user"] = request.user

        quote = serializer.save()
        data["invoice_no"] = 10000 + quote.id
        
        filename=f'Code4Kids {self._type} - {data["invoice_no"]}.pdf'
        
        pdf = self.createPdf(data)
        data["pdf_file"] = ContentFile(pdf.getvalue(), filename)

        serializer.save()
        # return FileResponse(pdf, as_attachment=True, filename=filename)
        return redirect("dwitter:upload_file")

    
    @swagger_auto_schema(auto_schema=None)
    def get(self, request, *args, **kwargs):
        form = QuoteForm(request.POST or None, initial = default_val)
        user = request.user

        return render(request, 'upload.html', {"form": form, "user": user})


CURRENCY_MAP = {
    "ZAR": "R",
    "USD": "$",
    "GBP": "£",
    "EUR": "€",
    "AUD": "$",
    "NZD": "$",
    "INR": "₹",
}
