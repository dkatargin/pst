from django.urls import path
from poster.views import post, get_post

urlpatterns = [
    path(r'', post),
    path('<uuid:post_id>/', get_post),
]
