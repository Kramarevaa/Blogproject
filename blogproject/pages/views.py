from django.shortcuts import render

# Create your views here.
def index(requests):
    context = {}
    return render(request, 'pages/index.html', context=context)