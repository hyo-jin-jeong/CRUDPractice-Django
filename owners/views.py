from django.views import View
from django.http import JsonResponse
from .models import Owner, Dog

# Create your views here.
class NewOwnersView(View):
    def post(self, request):
        data = json.loads(request.body)

        name = data['name']
        email = data['email']
        age = data['age']

