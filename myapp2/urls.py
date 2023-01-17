from django.urls import path
from myapp2.views import view_ad_mail

urlpatterns = [
    path('adv/', view_ad_mail, name="ad" ),
]