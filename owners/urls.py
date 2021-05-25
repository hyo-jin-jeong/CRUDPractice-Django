from django.urls import path
from .views import NewDogsView, NewOwnersView, OwnerListView

urlpatterns = [
    path('/addowner', NewOwnersView.as_view()),
    path('/adddog', NewDogsView.as_view()),
    path('/getowners', OwnerListView.as_view())
]
