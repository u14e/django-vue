from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import VerifyCode
from .serializers import (
    VerifyCodeSerializer,
    UserRegisterSerializer,
    UserSerializer
)

User = get_user_model()


class VerifyCodeViewSet(mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    serializer_class = VerifyCodeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = dict(
            code='1234',
            phone=serializer.validated_data['phone']
        )
        m = VerifyCode(**data)
        m.save()

        return Response(m.phone, status=status.HTTP_201_CREATED)


class UserRegisterViewSet(mixins.CreateModelMixin,
                          viewsets.GenericViewSet):
    serializer_class = UserRegisterSerializer


class UserViewSet(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


