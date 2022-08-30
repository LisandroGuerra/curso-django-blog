from email import message
from django.contrib import admin

from website.models import Post, Contact


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'author', 'categories', 'approved')

    def get_queryset(self, request):
        return Post.objects.filter(approved=True)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')

    def get_queryset(self, request):
        return Contact.objects.all()


admin.site.register(Post, PostAdmin)
admin.site.register(Contact, ContactAdmin)
