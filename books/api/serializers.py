from rest_framework.serializers import ModelSerializer, Serializer, CharField
from books.models import Books

class BooksSerializer(ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'  # Serializa todos los campos del modelo Books
        # Puedes especificar campos específicos si lo prefieres, por ejemplo:
        # fields = ['id', 'title', 'author', 'aviableCopies']

class BooksCreateSerializer(Serializer):
    title = CharField()
    author = CharField()