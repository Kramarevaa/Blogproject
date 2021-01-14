from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from blogs.models import Blog
# Create your views here.
@login_required
def index(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'pages/index.html', context=context)