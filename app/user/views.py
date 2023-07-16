""" Views for the user API """

from rest_framework import generics, authentication, permissions, views, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from user.serializers import UserSerializer, AuthTokenSerializer
from rest_framework.response import Response
from django.contrib.auth import authenticate, login


class CreateUserView(generics.CreateAPIView):
    """ Create a new user in the system. """
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)


class CreateTokenView(ObtainAuthToken):
    """ Create a new auth token for user. """
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user."""
    serializer_class = UserSerializer
    authentication_classes = [
        authentication.TokenAuthentication, authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrive and return the authenticated user."""
        return self.request.user


class LoginUserView(views.APIView):
    """ Serializer for logging users with session id """
    # authentication_classes = [authentication.SessionAuthentication]
    permission_classes = (permissions.AllowAny,)
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    def post(self, request):
        serializer = AuthTokenSerializer(data=self.request.data, context={
                                         'request': self.request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            return Response(None, status=status.HTTP_202_ACCEPTED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
