from django.urls import path, include
from .views import dashboard, profile_list, profile, upload_file, QuoteView

app_name = "dwitter"

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("profile_list/", profile_list, name="profile_list"),
    path("profile/<int:pk>", profile, name="profile"),
    path("accounts/", include("django.contrib.auth.urls")),
    # path("upload/", upload_file, name="upload_file"),
    path("upload/", QuoteView.as_view(), name="upload_file"),
]