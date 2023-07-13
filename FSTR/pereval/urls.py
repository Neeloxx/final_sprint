from django.urls import path
from .views import PerevalListView, SubmitDataViewSet, PerevalUpdateView

urlpatterns = [
    path('pereval/', PerevalListView.as_view(), name='user'),
    path('submitData/', SubmitDataViewSet.as_view(), name='list_or_create'),
    path('submitData/<int:pk>/', PerevalUpdateView.as_view(), name='read_update')

]
