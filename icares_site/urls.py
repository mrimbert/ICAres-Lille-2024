from django.urls import path

from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("", views.index, name="index"),
    path("epreuve", views.epreuve, name="epreuve")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)