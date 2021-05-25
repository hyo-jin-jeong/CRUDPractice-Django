import json

from django.views import View
from django.http import JsonResponse
from .models import Owner, Dog

# Create your views here.
class NewOwnersView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            name = data['name']
            email = data['email']
            age = data['age']

            Owner.objects.create(name=name, email=email, age=age)

            return JsonResponse({'message':'SUCCESS!'}, status=201)

        except KeyError:
            return JsonResponse({'message':'INVALID_KEY'}, status=400)
