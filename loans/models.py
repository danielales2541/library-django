from django.db import models
from books.models import Books
from Users.models import Users
# Create your models here.
class loans(models.Model):
    loansdate = models.DateField()
    returnDate = models.DateField(null=True, blank=True)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
