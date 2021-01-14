from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from profiles.models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required
def user_profile_page(request, username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    context = {
        'profile': profile
    }
    return render(request, 'profiles/profile.html', context=context)

@login_required
def user_profile_edit_page(request, username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    context = {
        'profile': profile
    }
    if request.method == 'GET':
        if request.user.username != user.username:
            messages.error(request, "You can't edit stranger' s profile")
            return redirect('/profiles/profile/{}'.format(user.username))
        return render(request, 'profiles/profile_edit.html', context=context)
   
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        status = request.POST['status']
        about = request.POST['about']
        # user update
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
        # profile update
        profile.status = status
        profile.about = about
        try:
            if any(request.FILES):
                profile.profile_image = request.FILES['profile_image']
        except:
             messages.error(request, 'Profile Image is not correct!')
             return render(request, 'profiles/profile_edit.html', context=context)
        user.save()
        profile.save()
        messages.success(request, 'Profile successfully changed!')
        return redirect('/profiles/profile/{}'.format(user.username))


