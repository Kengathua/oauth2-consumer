from rest_framework.fields import ReadOnlyField, SerializerMethodField, CharField
from rest_framework.serializers import ModelSerializer

from oauth2_consumer.users.models import User

class UserSerializer(ModelSerializer):
    """Serialize a user, their roles and their permissions."""

    full_name = ReadOnlyField(source='get_full_name', read_only=True)
    roles = CharField(required=False, allow_null=True)
    permissions = CharField(required=False, allow_null=True)

    class Meta:
        """Exclude sensitive fields (e.g password) from being serialized for a user."""

        model = User
        fields = (
            'id', 'first_name', 'last_name', 'other_names',
            'full_name', 'phone_no', 'email', 'date_of_birth',
            'date_joined', 'is_staff', 'is_admin', 'is_active',
            'guid', 'updated_on',)

class MeSerializer(UserSerializer):
    """A special serializer used to serialize the details of the logged in user."""

    class Meta(UserSerializer.Meta):
        """Link the MeSerializer to it's parent's Meta."""

        fields = UserSerializer.Meta.fields
