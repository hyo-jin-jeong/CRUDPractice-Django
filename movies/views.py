
from django.views import View
from django.http import JsonResponse
from .models import *


# Create your views here.
class MovieListView(View):
    def get(self,request):
        movie_list = Movie.objects.all()
        result = []
        for movie in movie_list:

            actors = [{
                'name':actor.last_name
            }for actor in movie.actor.all()]

            movie_info = {
                'title' : movie.title,
                'running_time' : movie.running_time,
                'actor_list': actors
            }
            result.append(movie_info)
        return JsonResponse({'result' :  result}, status=200)
        

class ActorListView(View):
    def get(self, request):
        actor_list = Actor.objects.all()
        result = []
        for actor in actor_list:

            movies = [{
                'title':m.title
            }for m in actor.movies.all()]

            actor_info = {
                'first_name':actor.first_name,
                'last_name':actor.last_name,
                'movies': movies
            }
            result.append(actor_info)
        return JsonResponse({'result': result}, status=200)


        

        

