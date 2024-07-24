from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import (
    ListView,
    DetailView,
    FormView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post
from django.shortcuts import get_object_or_404
from .forms import PostForm
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)


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
    """
    a class based view to show index page
    """

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "Abbas"
        context["posts"] = Post.objects.all()
        return context


# Function-Based View for redirect
"""

from django.shortcuts import redirect
def redirectToMaktab(request):
    return redirect('https://maktabkhooneh.org/')

"""


class RedirectToMaktab(RedirectView):
    url = "https://maktabkhooneh.org/"

    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs.get("pk"))
        print(post)
        return super().get_redirect_url(*args, **kwargs)


class PostListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = "blog.view_post"
    # model = Post
    queryset = Post.objects.all()

    # def get_queryset(self):
    #     posts = Post.objects.filter(status = True)
    #     return posts

    ordering = "-id"

    context_object_name = "posts"
    # paginate_by = 2


class PostListApiView(TemplateView):
    template_name = "blog/post_list_api.html"


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post


"""
class PostCreateView(FormView):
    template_name = 'contact.html'
    form_class = PostForm
    success_url = '/blog/post/'

    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
 """


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # fields = ['author','title','content','status','category','published_date']
    form_class = PostForm
    success_url = "/blog/post/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostEditView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    success_url = "/blog/post/"


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = "/blog/post/"
