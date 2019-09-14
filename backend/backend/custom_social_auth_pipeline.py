import re
from django.core.exceptions import PermissionDenied
from social_core.exceptions import AuthFailed

USER_FIELDS = ['username', 'email']


def allowed_email(email):
    return re.match('.*@acme\.com', email) or \
        re.match('.*@acme\.net', email)


def create_user(strategy, details, backend, user=None, *args, **kwargs):
    
    if user:
        return {'is_new': False}

    
    fields = dict((name, kwargs.get(name, details.get(name)))
                  for name in backend.setting('USER_FIELDS', USER_FIELDS))
    print(fields)

    WHITE_LIST = set(['myachin2002'])

    if fields.get("username", "you-che-daun") not in WHITE_LIST:
        PermissionDenied()
        return

    
    if not fields:
        return

    if not allowed_email(fields['email']):
        return

    return {
        'is_new': True,
        'user': strategy.create_user(**fields)
    }