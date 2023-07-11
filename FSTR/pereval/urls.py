from django.urls import path
from .views import UserViewSet, CoordsViewSet

urlpatterns = [
    path('user/', UserViewSet.as_view(), name='user'),
    path('coords/', CoordsViewSet.as_view(), name='coords'),

]
