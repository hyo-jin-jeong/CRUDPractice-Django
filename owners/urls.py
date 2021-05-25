from django.urls import path
from .views import NewDogsView, NewOwnersView

urlpatterns = [
    path('/addowner', NewOwnersView.as_view())
    ,path('/adddog', NewDogsView.as_view())
]
