from django.contrib import admin
from .models import Post

admin.site.register(Post)

SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'first_name', 'email']
