from django.urls import path
from website.views import home, post_detail, save_form


urlpatterns = [
    path('', home, name='home'),
    path('post/<int:id>/', post_detail, name='post_detail'),
    path('save-form', save_form, name='save_form'),
]
