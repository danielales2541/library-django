from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from loans.models import loans
from Users.models import Users
from books.models import Books
from loans.api.serializers import LoansSerializer, LoansCreateSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from django.utils import timezone
class LoansApiViewSet(ModelViewSet):
    """
    API endpoint that allows loans to be viewed or edited.
    """
    queryset = loans.objects.all()
    serializer_class = LoansSerializer
    permission_classes = [IsAuthenticated] 

    
    def create(self, request, *args, **kwargs):
        requestSerrializer = LoansCreateSerializer(data=request.data)
        if not requestSerrializer.is_valid():
            return Response(requestSerrializer.errors, status=status.HTTP_400_BAD_REQUEST)
        print("request: ", request.data)
        try:
          users= Users.objects.get(id= request.data['user_id'])
        except Users.DoesNotExist:   
           return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        try:
           book = Books.objects.get(id=request.data['book_id'])
        except Books.DoesNotExist:
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
        print("book: ", book.aviableCopies)
        try:
            loan = loans.objects.get(id= request.data['user_id'])
            print("loans es:", loan.loansdate)
        except loans.DoesNotExist:
            return Response({"loan not exist"}, status=status.HTTP_404_NOT_FOUND)
        return_date_str = request.data['returnDate']
        return_date = datetime.strptime(return_date_str, "%Y-%m-%d").date()
        if return_date < loan.loansdate:
            return Response({"The return date must not be earlier than the loan date."}, status= status.HTTP_404_NOT_FOUND)
        if book.aviableCopies == 0:
            return Response({"error": "no tengo copias papito :)"}, status=status.HTTP_404_NOT_FOUND)
        print("dato",return_date)
        loan.loansdate = return_date
        loan.save()
        book.aviableCopies = book.aviableCopies -1
        book.save()
        loan = loans(
             loansdate = timezone.now().date(),
             returnDate = return_date,
             book = book,
             user = users
        )
        loan.save()
        return Response({"message": "Préstamo procesado"}, status=200)

            
    @action(methods=['get'], detail=False, url_path=r"active/(?P<user_id>\d+)")
    def active_loans(self, request, user_id=None):
        """
        Retrieve all active loans for a specific user.
        """
        if not user_id:
            return Response({"error": "User ID is required"}, status=status.HTTP_400_BAD_REQUEST)
        #quitar el if que valida si existe el usuario, ya que si no existe no se puede hacer un préstamo
        if not Users.objects.filter(id=user_id).exists():
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        active_loans = loans.objects.filter(user_id=user_id,returnDate__isnull=True)
        

        if not active_loans.exists():
            return Response({"message": "No active loans found for this user"}, status=status.HTTP_404_NOT_FOUND)

        serializer = LoansSerializer(active_loans, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
       
   