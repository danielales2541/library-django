from rest_framework.routers import DefaultRouter
from Users.api.views import UsersApiViewSet

router_users = DefaultRouter()
router_users.register(prefix='users', basename='users', viewset=UsersApiViewSet)

