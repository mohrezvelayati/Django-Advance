from typing import Any
from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from .models import Post
from django.shortcuts import get_object_or_404


# Create your views here.

# Function-Based View for showing the template
"""
def indexView(request):
    '''
    a function based view to show index page
    '''
    name = "Abdullah"
    context = {"name":name}
    return render(request, "index.html", context)
"""


class IndexView(TemplateView):
    '''
    a class based view to show index page
    '''
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "Abbas"
        context["posts"] = Post.objects.all()
        return context
    


# Function-Based View for redirect
'''

from django.shortcuts import redirect
def redirectToMaktab(request):
    return redirect('https://maktabkhooneh.org/')

'''


class RedirectToMaktab(RedirectView):
    url = 'https://maktabkhooneh.org/'
    
    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs.get('pk'))
        print(post)
        return super().get_redirect_url(*args, **kwargs)