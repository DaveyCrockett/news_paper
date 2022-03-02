from django.urls import path

from pages.views import ContactPageView, ContactSuccessView
from .views import HomePageView, AboutPageView



urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('cont-success/', ContactSuccessView.as_view(), name="cont-success"),
] 