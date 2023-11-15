from django.urls import path
from .views import TemplatesViews

urlpatterns = [
    path('get_form', TemplatesViews.as_view())
]