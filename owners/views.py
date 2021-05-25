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


class OwnerListView(View):
    def get(self, request):
        owners = Owner.objects.all()

        result = []
        for owner in owners:
            result.append({'name' :owner.name, 'email' :owner.email, 'age':owner.age})
        # result = json.dumps(result)

        return JsonResponse({'result':result}, status=200)
