from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp
from oauth2_consumer.site_managers import serializers

class SiteViewSet(viewsets.ModelViewSet):
  permission_classes = (AllowAny,)
  queryset = Site.objects.all()
  serializer_class = serializers.SiteSerialzer


class SocialAppViewSet(viewsets.ModelViewSet):
  permission_classes = (AllowAny,)
  queryset = SocialApp.objects.all()
  serializer_class = serializers.SocialAppSerializer
