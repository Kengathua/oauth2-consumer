from allauth.socialaccount import providers
from allauth.socialaccount.app_settings import QUERY_EMAIL
from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider


class Scope(object):
    read = 'read'
    write = 'write'
    groups = 'groups'

class CustomAccount(ProviderAccount):
    pass


class CustomProvider(OAuth2Provider):

    id = 'provider'
    name = 'Portfolio Provider'
    account_class = CustomAccount

    def get_default_scope(self):
        scope = [Scope.read, Scope.write, Scope.groups]
        return scope

    def extract_uid(self, data):
        return str(data['guid'])

    def extract_common_fields(self, data):
        return dict(
                    email=data['email'],
                    first_name=data['first_name'],
                    last_name=data['last_name'],)


providers.registry.register(CustomProvider)