from django.urls import path
from .views import PerevalListView, SubmitDataViewSet

urlpatterns = [
    path('pereval/', PerevalListView.as_view(), name='user'),
    path('submitData/', SubmitDataViewSet.as_view(), name='list_or_create'),

]
