from django.shortcuts import render
from .models import Feature
# from django.http import HttpResponse

# Create your views here.
def index(request):
    # context = {
    #     'name': 'Silky',
    #     'age': 21,
    #     'nationality': 'Indian'
    # }

    # feature1 = Feature()
    # feature1.id = 0
    # feature1.name = 'Fast'
    # feature1.details = 'Our service is very quick'

    # once added to DB, no need to define them manually
    features = Feature.objects.all() ## list
    return render(request, 'index.html', {'features': features})

def counter(request):
    words = request.POST['words']
    numWords = len(words.split(' '))
    return render(request, 'counter.html', {'numWords': numWords})