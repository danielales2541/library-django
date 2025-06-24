from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from books.models import Books
from books.api.serializers import BooksSerializer, BooksCreateSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
class BooksApiViewSet(ModelViewSet):
    """
    API endpoint that allows books to be viewed or edited.
    """
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    permission_classes = [IsAuthenticated]  # Asegura que solo usuarios autenticados puedan acceder a esta vista

    def create(self, request, *args, **kwargs):
        requestSerializer = BooksCreateSerializer(data=request.data)
        if not requestSerializer.is_valid():
            return Response(requestSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
         
        if Books.objects.filter(title=request.data['title']).exists():
            return Response({"error", "titulo en existencia"},status=status.HTTP_409_CONFLICT)            
        try:    
            book = Books(
            title = request.data['title'],
            author = request.data['author']
            )
            book.save()
        except IntegrityError as e: 
            Response({"error": f"Error al guardar el libro debido a un problema de integridad de datos: {e}"})
     
        return Response({"mensaje":"Book create sucefull"},status=status.HTTP_201_CREATED)
    
    @action(methods=['get'], detail=False, url_path="search")
    def search_books(self, request):
        """
        Retrieve all active loans for a specific user.
        """
        title = request.query_params.get('title')
        if not title:
            return Response({"error": "title is required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            book = Books.objects.get(title=title)
        except Books.DoesNotExist:    
            return Response({"error": "title not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = BooksSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
       

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object() 
            instance.delete() 
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Books.DoesNotExist:
            return Response(
                {"error": "El libro con ese ID no existe."},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"error": f"Ocurrió un error inesperado al eliminar el libro: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
