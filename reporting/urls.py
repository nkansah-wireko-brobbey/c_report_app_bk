from django.urls import path
from .views import DynamicQueryView
from .views import metadata_view

urlpatterns = [
    path("reporting/", DynamicQueryView.as_view(), name="reporting"),
    path("metadata/", metadata_view, name="metadata")
]
