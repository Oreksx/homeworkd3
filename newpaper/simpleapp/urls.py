from django.urls import path
from simpleapp.views import NewList, NewDetail

urlpatterns = [
    path('', NewList.as_view()),
    path('<int:pk>', NewDetail.as_view()),
]

















