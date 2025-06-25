from rest_framework.routers import DefaultRouter
from loans.api.views import LoansApiViewSet

loans_router = DefaultRouter()  
loans_router.register(prefix='loans', basename='loans', viewset=LoansApiViewSet)