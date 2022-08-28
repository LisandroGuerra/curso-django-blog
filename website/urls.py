from django.urls import path

from website.views import hello_website


urlpatterns = [
    path('', hello_website),
]
