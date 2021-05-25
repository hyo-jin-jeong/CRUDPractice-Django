from django.urls import path
from .views import *

urlpatterns = [
    path('/getactors', ActorListView.as_view()),
    path('/getmovies', MovieListView.as_view()),
]
