from django.urls import path
from authentication.views import *

urlpatterns = [
    path('signup/', UserRegistrationAPIView.as_view(), name='signup'),
]
