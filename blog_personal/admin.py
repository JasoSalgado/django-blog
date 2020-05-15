from django.contrib import admin
#Import Post to make it visible in the admin page
from .models import Post

admin.site.register(Post)
