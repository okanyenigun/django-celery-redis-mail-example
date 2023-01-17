from django.urls import path
from myapp.views import IndexView
urlpatterns = [
    path('', IndexView.as_view(), name="index" ),
]