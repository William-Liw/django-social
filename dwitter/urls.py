from django.urls import path, include
from .views import dashboard, profile_list, profile, upload_file, QuoteView
from django.conf import settings
from django.conf.urls.static import static

app_name = "dwitter"

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("profile_list/", profile_list, name="profile_list"),
    path("profile/<int:pk>", profile, name="profile"),
    path("accounts/", include("django.contrib.auth.urls")),
    # path("upload/", upload_file, name="upload_file"),
    path("upload/", QuoteView.as_view(), name="upload_file"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)