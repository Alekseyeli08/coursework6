from django.shortcuts import render
from blog.models import Blog
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify
from django.shortcuts import get_object_or_404, redirect
from blog.forms import BlogForm
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.services import get_blog_from_cache
class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog:blog_create')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()
        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogForm

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:blog_detail', kwargs={'pk': self.object.pk})


class BlogListView(LoginRequiredMixin, ListView):
    model = Blog

    def get_queryset(self):
        return get_blog_from_cache()



class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_views += 1
        self.object.save()
        return self.object


class BlogDeleteView(DeleteView):
    model = Blog
    fields = ('title', 'content', 'image')
    success_url = reverse_lazy('blog:blog_list')


def is_published(request, pk):
    is_published_blog = get_object_or_404(Blog, pk=pk)
    if is_published_blog:
        is_published_blog = False
    else:
        is_published_blog = True

    is_published_blog.save()

    return redirect(reverse('blog:blog_list'))
