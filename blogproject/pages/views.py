from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from blogs.models import Blog
from django.core.paginator import Paginator
from taggit.models import Tag


# Create your views here.
@login_required
def index(request):
    blogs = Blog.objects.all()

    latest_blogs = blogs.order_by('-created_at')[:4]

    if request.method == 'GET':
        search = request.GET.get('search', '')
        if search:
            blogs = blogs.filter(text__icontains=search)

        sort_by = request.GET.get('sort_by', '')
        if sort_by:
            sort_by_dict = {
                'a-z': 'title',
                'z-a': '-title',
                'new-old': '-created_at',
                'old-new': 'created_at'
            }
            sort_by_param = sort_by_dict.get(sort_by)
            blogs = blogs.order_by(sort_by_param)
        filter_by_tag = request.GET.get('filter_by_tag', '')
        if filter_by_tag:
            blogs = blogs.filter(tags__name__icontains=filter_by_tag)

    # paginator
    paginator = Paginator(blogs, 10) # Show 2 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    tags = Tag.objects.all()

    all_tags = ",".join([t.name for t in tags]).replace(" ","").split(",")

    context = {
        'blogs': blogs,
        'latest_blogs': latest_blogs,
        'page_obj': page_obj,
        'all_tags': all_tags
    }
    return render(request, 'pages/index.html', context=context)