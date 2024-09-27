from django.urls import path

from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("", views.index, name="index"),
    path("epreuve", views.epreuve, name="epreuve"),
    path("detail/<id>", views.detail, name="detail"),
    path("inscription", views.register, name="inscription"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)