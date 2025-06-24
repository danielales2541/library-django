from django.contrib import admin

# Register your models here.
from books.models import Books

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    pass

