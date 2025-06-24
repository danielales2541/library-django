from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from Users.models import Users
from rest_framework.permissions import AllowAny
from Users.api.serializers import UsersSerializer, UsersCreateSerializer
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
class UsersApiViewSet(ModelViewSet):
    """
    API endpoint that allows books to be viewed or edited.
    """
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [AllowAny]  # Asegura que solo usuarios autenticados puedan acceder a esta vista

    
    def create(self, request, *args, **kwargs):
        requestSerializer = UsersCreateSerializer(data=request.data)
        if not requestSerializer.is_valid():
            return Response(requestSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        if Users.objects.filter(correo=request.data['correo']).exists():
            return Response({"error", "correo en existencia"},status=status.HTTP_409_CONFLICT)        
        if Users.objects.filter(nombre=request.data['nombre']).exists():
            return Response({"error", "usuario  en existencia"},status=status.HTTP_409_CONFLICT) 
        try:
            user = Users(
            nombre = request.data['nombre'],
            correo = request.data['correo']
            )
            user.save()    
        except IntegrityError as e: 
            Response({"error": f"Error al guardar el libro debido a un problema de integridad de datos: {e}"})
        return Response({"mensaje":"Usuario registrado correctamente."},status=status.HTTP_201_CREATED)

        