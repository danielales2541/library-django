from rest_framework.serializers import ModelSerializer,Serializer, CharField,EmailField
from Users.models import Users

class UsersSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'  # Serializa todos los campos del modelo Books
        # Puedes especificar campos específicos si lo prefieres, por ejemplo:
        # fields = ['id', 'title', 'author', 'aviableCopies']


class UsersCreateSerializer(Serializer):
    nombre = CharField()
    correo= CharField()