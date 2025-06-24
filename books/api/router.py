from rest_framework.routers import DefaultRouter
from books.api.views import BooksApiViewSet

books_router = DefaultRouter()
books_router.register(prefix='books', basename='books', viewset=BooksApiViewSet)

