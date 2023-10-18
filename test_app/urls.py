from django.urls import path

from .views import *

urlpatterns = [
    path('', test_app),
    path('register/', register_view),
    path('login/', login_view),
    path('logout/', logout_view)
]