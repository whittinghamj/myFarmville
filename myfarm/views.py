from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all
    }
    return render(request, 'myfarm/home.html', context)
    #Alternative: HttpResponse('<h1>Django Test Home<h1>')

def about(request):
    return render(request, 'myfarm/about.html', {'title': 'About'})
    #return HttpResponse('<h1>Django Test About <h1>')