from django.contrib import admin

# Register your models here.
from .models import Pic,Post

admin.site.register(Pic)
admin.site.register(Post)