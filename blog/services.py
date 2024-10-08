from config.settings import CACHE_ENABLED
from blog.models import Blog
from django.core.cache import cache

def get_blog_from_cache():
    if not CACHE_ENABLED:
        return Blog.objects.all()
    key = 'category_list'
    blog = cache.get(key)
    if blog is not None:
        return blog
    blog = Blog.objects.all()
    cache.set(key, blog)

    return blog
