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


class NewDogsView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            owner_email = data['owner_email']
            name = data['name']
            age = data['age']

            owner = Owner.objects.get(email = owner_email)
            Dog.objects.create(owner = owner, name=name, age=age)

            return JsonResponse({'message' : 'SUCCESS!'}, status=201)

        except KeyError:
            return JsonResponse({'message' : 'INVALID_KEY'}, status=400)
        
        except Owner.DoesNotExist:
            return JsonResponse({"message":'USER DOES NOT EXIST'}, status=404)

class OwnerListView(View):
    def get(self, request):
        owners = Owner.objects.all()
        result = []
        for owner in owners:
            dogs = {}
            dog_objects = owner.dog.all()
            for dog in dog_objects:
               dogs[dog.id] = {'name':dog.name, 'age':dog.age} 
            result.append({'name' :owner.name, 'email' :owner.email, 'age':owner.age, 'dogs':dogs})
        
        return JsonResponse({'result':result}, status=200)

class DogListView(View):
    def get(self, request):
        dogs = Dog.objects.all()
        owners = Owner.objects.all()
        result = []
        for dog in dogs:
            result.append({'name':dog.name, 'age':dog.age, 'owner_name':dog.owner.name}) 

        return JsonResponse({'result':result}, status=200)