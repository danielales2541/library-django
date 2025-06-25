from django.contrib import admin
from loans.models import loans
# Register your models here.
@admin.register(loans)
class loansAdmin(admin.ModelAdmin):
    pass