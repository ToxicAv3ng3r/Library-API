from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import BookAuthorListViewSet, AuthorListViewSet, BookListViewSet


v1_router = SimpleRouter()
v1_router.register(
    'book',
    BookAuthorListViewSet,
    basename='book'
)
v1_router.register(
    'authors',
    AuthorListViewSet,
    basename='authors'
)
v1_router.register(
    'books',
    BookListViewSet,
    basename='books'
)

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/', include('djoser.urls.jwt'))
]
