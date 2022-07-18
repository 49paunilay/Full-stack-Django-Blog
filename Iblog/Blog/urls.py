from django.urls import path
from .views import home,contact_information, singlePostInformation
urlpatterns = [
    path('',home),
    path('contact',contact_information),
    path('<slug:url>',singlePostInformation)
]