from django.urls import path
from .views import NewOwnersView

urlpatterns = [
    path('', NewOwnersView.as_view())
]
