from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    UpdateModelMixin,
    DestroyModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    ListModelMixin
)

from rest_framework import authentication, permissions
from problem.models import Problem
from problem.serializer import ProblemSerializer


class GetProblemListView(GenericAPIView, ListModelMixin):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class GetProblemView(GenericAPIView, RetrieveModelMixin):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CreateProblemView(GenericAPIView, CreateModelMixin):
    queryset = Problem.objects.all()

    serializer_class = ProblemSerializer

    authentication_classes = [
        authentication.SessionAuthentication,
        authentication.TokenAuthentication
    ]

    permission_classes = [
        permissions.IsAuthenticated & permissions.IsAdminUser]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ModifyProblem(GenericAPIView, UpdateModelMixin, DestroyModelMixin):

    permission_classes = [
        permissions.IsAuthenticated & permissions.IsAdminUser]
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    # def get_object(self):
