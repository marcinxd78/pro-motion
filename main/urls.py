
from django.urls import path
from .views import all_proms
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', all_proms )
]