from django.urls import path

from website.views import home, post_detail


urlpatterns = [
    path('', home, name='home'),
    path('post/<int:id>/', post_detail, name='post_detail'),
]
