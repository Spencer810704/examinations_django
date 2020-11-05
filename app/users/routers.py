from rest_framework import routers
from users.viewsets import MyUserViewSet

router = routers.SimpleRouter()
router.register('users', MyUserViewSet)
