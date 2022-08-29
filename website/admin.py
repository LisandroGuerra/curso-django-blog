from django.contrib import admin

from website.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'author', 'categories', 'approved')

    def get_queryset(self, request):
        return Post.objects.filter(approved=True)


admin.site.register(Post, PostAdmin)
