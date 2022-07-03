from rest_framework import viewsets
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from oauth2_consumer.users import serializers
from oauth2_consumer.users.models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class MeView(RetrieveAPIView):
    """Return the details of the currently logged in user."""

    permission_classes = (IsAuthenticated,)
    queryset = User.objects.none()
    serializer_class = serializers.MeSerializer

    def get_object(self):
        """Limit this view to only return the logged in user's details."""
        return self.request.user

@login_required()
def home(request, *args, **kwargs):
    full_name = f'{request.user.first_name} {request.user.last_name}'
    return HttpResponse(f'Hello {full_name}!, You have successfully signed in using the oauth2 server!', status=200)
