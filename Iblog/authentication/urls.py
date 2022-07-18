from django.urls import path
from .views import signin,signup,forgetpassword,signout

urlpatterns = [
    path('signin',signin),
    path('signup',signup),
    path('forgetpassword',forgetpassword),
    path('logout',signout)
]