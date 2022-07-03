import json
import requests
from django.conf import settings
from oauth2_consumer.users.models import User
from allauth.socialaccount.providers.oauth2.views import (
    OAuth2Adapter,
    OAuth2LoginView,
    OAuth2CallbackView,
    )
from oauth2_consumer.portfolioprovider.provider import CustomProvider


class CustomAdapter(OAuth2Adapter):
    provider_id = CustomProvider.id
    # Fetched programmatically, must be reachable from container
    access_token_url = '{}/o/token/'.format(settings.OAUTH_SERVER_BASEURL)
    profile_url = '{}/v1/users/profile/'.format(settings.OAUTH_SERVER_BASEURL)

    # Accessed by the user browser, must be reachable by the host
    authorize_url = '{}/o/authorize/'.format('http://localhost:9000')
    emails_url = "{0}/user/emails".format(settings.OAUTH_SERVER_BASEURL)
    # redirect_uri_protocol = "https"
    redirect_uri_protocol = "http"

    # NOTE: trailing slashes in URLs are important, don't miss it

    def complete_login(self, request, app, token, **kwargs):
        headers = {'Authorization': 'Bearer {0}'.format(token.token)}
        resp = requests.get(self.profile_url, headers=headers)
        extra_data = resp.json()
        user_data = json.loads(resp.content)
        user = User.objects.filter(email=user_data['email'])
        if user.exists():
            ignore_fields = []
            # ignore_fields = ['guid', 'other_names']
            user_data = {key:val for key, val in user_data.items() if key not in ignore_fields}
            user.update(**user_data)
            # return self.get_provider().sociallogin_from_response(request, extra_data)

        return self.get_provider().sociallogin_from_response(request, extra_data)

    def get_email(self, headers):
        email = None
        resp = requests.get(self.emails_url, headers=headers)
        resp.raise_for_status()
        emails = resp.json()
        if resp.status_code == 200 and emails:
            email = emails[0]
            primary_emails = [
                e for e in emails if not isinstance(e, dict) or e.get("primary")
            ]
            if primary_emails:
                email = primary_emails[0]
            if isinstance(email, dict):
                email = email.get("email", "")
        return email


oauth2_login = OAuth2LoginView.adapter_view(CustomAdapter)
oauth2_callback = OAuth2CallbackView.adapter_view(CustomAdapter)
