from django.shortcuts import render, redirect
from blogs.models import Blog
from profiles.models import Profile
from comments.models import Comment
import json
from django.http import HttpResponse

# Create your views here.
def single_blog(request, blog_id):
    blog = Blog.objects.get(id=str(blog_id))
    profile = Profile.objects.get(user=request.user)
    context = {
        'blog': blog,
        'profile': profile,
        
    }
    return render(request, 'blogs/single_blog.html', context=context)

def leave_comment_to_blog(request, blog_id):
    if request.method == 'POST':
        blog = Blog.objects.get(id=str(blog_id))
        profile = Profile.objects.get(user=request.user)
        comment = Comment()
        comment.author = profile
        comment.text = request.POST.get('text', '---')
        comment.save()
        blog.comments.add(comment)
        blog.save()
        return redirect('single_blog', blog_id=blog_id)
def add_or_remove_like(request, blog_id):
    blog = Blog.objects.get(id=str(blog_id))
    profile = Profile.objects.get(user=request.user)
    #Обращение к списку лайков
    if profile.id in blog.likes:
        blog.likes.remove(profile.id)
    else:
        blog.likes.append(profile.id)
    blog.save()
    return redirect('single_blog', blog_id=blog_id)

def add_or_remove_like_ajax(request):
    if request.is_ajax():
        blog_id = request.POST.get('blog_id')
        blog = Blog.objects.get(id=str(blog_id))
        profile = Profile.objects.get(user=request.user)
        like_color = ''
        if profile.id in blog.likes:
            blog.likes.remove(profile.id)
            like_color = 'empty'
        else:
            blog.likes.append(profile.id)
            like_color = 'red'
        blog.save()
        return HttpResponse(json.dumps({'likes': len(blog.likes), 'like_color': like_color}),  content_type='application/json')



