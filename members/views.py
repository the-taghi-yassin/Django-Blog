from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import *
from index.models import *
from django.views import generic


def favourite_add(request, id):
    post = get_object_or_404(Post, id=id)
    if post.favourites.filter(id=request.user.id).exists():
        post.favourites.remove(request.user)
    else:
        post.favourites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url= reverse_lazy('login')

def profile(request):
    new = Post.newmanager.filter(favourites=request.user)
    cats = Category.objects.all().order_by('-id')
    post = Post.newmanager.all().order_by('-id')
    return render(request,'registration/profile.html',{'post':post, 'cats':cats, 'new': new})

class ProfileEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/profile_edit.html'
    success_url= reverse_lazy('profile')
    def get_object(self):
        return self.request.user
    
class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url= reverse_lazy('profile-edit')