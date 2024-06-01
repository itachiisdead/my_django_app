from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context={
        'name': 'heba',
        'age': 20,
    }
    return render(request, 'index.html', context)

def about(request):
    text= request.GET['texts']
    num_of_words=len(text.split())
    return render(request, 'about.html', {'num_of_words': num_of_words})