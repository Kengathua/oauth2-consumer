import email
import logging
from django.conf import settings
from django.core.exceptions import MultipleObjectsReturned

from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.account.utils import (
    complete_signup,
    perform_login,)

from allauth.utils import (
    build_absolute_uri,
    email_address_exists,
    generate_unique_username,
    get_user_model,
    import_attribute,
)
LOGGER = logging.getLogger(__name__)

class SocialAccountAdapter(DefaultSocialAccountAdapter):

    def authentication_error(self, request, provider_id, error, exception, extra_context):
        msg = 'SocialAccount authentication error!',
        extra_data = {'provider_id': provider_id, 'error': error.__str__(), 'exception': exception.__str__(), 'extra_context': extra_context},
        LOGGER.info('{} {} {} {}'.format(msg, error, request, extra_data))
        raise exception

    def is_auto_signup_allowed(self, request, sociallogin):
        return True

    def pre_social_login(self, request, sociallogin):
        user = sociallogin.user
        if user.email:
            from oauth2_consumer.users.models import User
            try:
                existing_user = User.objects.get(email=user.email)
                perform_login(request, existing_user, settings.SOCIALACCOUNT_EMAIL_VERIFICATION)
                return
            except User.DoesNotExist:
                pass
        else:
            pass

    def save_user(self, request, sociallogin, form=None):
        user = sociallogin.user
        if not get_user_model().objects.filter(email=user.email).exists():
            sociallogin.save(request)
