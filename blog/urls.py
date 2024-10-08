from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView, BlogListView, is_published
from django.views.decorators.cache import cache_page


app_name = BlogConfig.name


urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='blog_create'),
    path('', BlogListView.as_view(), name='blog_list'),
    path('view/<int:pk>/', cache_page(60)(BlogDetailView.as_view()), name='blog_detail'),
    path('edit/<int:pk>/update/', BlogUpdateView.as_view(), name='blog_update'),
    path('delete/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
    path('activity/<int:pk>/', is_published, name='is_published'),


]