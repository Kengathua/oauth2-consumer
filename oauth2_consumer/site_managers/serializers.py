from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp
from rest_framework.serializers import ModelSerializer


class SiteSerialzer(ModelSerializer):
    """Serialer for adding all auth sites."""

    class Meta:
        """Meta class for site serializer."""
        model = Site
        fields = "__all__"


class SocialAppSerializer(ModelSerializer):
    """Serialer for adding allauth SocialApps."""

    class Meta:
        """Meta class for SocialApp serializer."""
        model = SocialApp
        fields = "__all__"