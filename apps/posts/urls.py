from django.urls import path
from apps.posts.api.views import PostCreate, PostList, PostRetrieve


urlpatterns = [
    path('', PostList.as_view()),
    path('<int:id>', PostRetrieve.as_view()),
    path('create', PostCreate.as_view()),
]