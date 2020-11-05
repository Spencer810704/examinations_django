from django.http import Http404
from rest_framework import mixins, status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.serializers import UserSerializer


class MyUserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            result = {
                'status': 'delete success!'
            }
        except Http404:
            result = {
                'status': 'no record, delete failed!'
            }

        finally:
            return Response(data=result, status=status.HTTP_204_NO_CONTENT)
