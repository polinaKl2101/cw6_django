from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from main.forms import BlogPostForm
from main.models import BlogPost


class BlogPostListView(generic.ListView):
    model = BlogPost
    template_name = 'main/blogpost/blogpost_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True)


class BlogPostCreateView(generic.CreateView):
    model = BlogPost
    template_name = 'main/blogpost/blogpost_create.html'
    form_class = BlogPostForm
    success_url = reverse_lazy('main:blogpost')


class BlogPostUpdateView(generic.UpdateView):
    model = BlogPost
    template_name = 'main/blogpost/blogpost_update.html'
    form_class = BlogPostForm
    success_url = reverse_lazy('main:blogpost')


class BlogPostDetailView(generic.DetailView):
    model = BlogPost
    template_name = 'main/blogpost/blogpost_detail.html'
    context_object_name = 'post'
    success_url = reverse_lazy('main:blogpost')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.views_count += 1
        self.object.save()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        return context_data


class BlogPostDeleteView(generic.DeleteView):
    model = BlogPost
    template_name = 'main/blogpost/blogpost_confirm_delete.html'
    success_url = reverse_lazy('main:blogpost')