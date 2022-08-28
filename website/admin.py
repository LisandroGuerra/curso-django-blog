from django.contrib import admin

from website.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'sub_title')


admin.site.register(Post, PostAdmin)
