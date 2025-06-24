from rest_framework.serializers import ModelSerializer, Serializer, IntegerField,DateField
from loans.models import loans
from Users.api.serializers import UsersSerializer
from books.api.serializers import BooksSerializer

class LoansSerializer(ModelSerializer):
    user= UsersSerializer(read_only=True)
    book = BooksSerializer(read_only=True)
    #se agrega esto
    loansdate =  DateField(format="%Y-%m-%dT%H:%M:%S.%fZ")
    returnDate =  DateField(format="%Y-%m-%dT%H:%M:%S.%fZ", required=False, allow_null=True)
    class Meta:
        model = loans
        fields = '__all__'  # Serializa todos los campos del modelo Loans
        # Puedes especificar campos específicos si lo prefieres, por ejemplo:
        # fields = ['id', 'book', 'user', 'loan_date', 'return_date']

class LoansCreateSerializer(Serializer):
    book_id = IntegerField()
    user_id = IntegerField()
    returnDate = DateField()

    