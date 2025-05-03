from rest_framework.authentication import TokenAuthentication
from django.utils.translation import gettext_lazy as _
from common.response import ResponseInfo
from common.exceptions import AuthenticationError
from common.utils.auth_utils import get_authorization_header


class TokenInQueryAuthentication(TokenAuthentication):
    """
    Extending token authentication,
    now you can pass tokens as GET or Header parameter
    """
    msg = ResponseInfo().response

    def authenticate(self, request):
        auth = get_authorization_header(request).split()
        if not auth or auth[0].lower() != b'token':
            return None

        if len(auth) == 1:
            self.msg["message"] = _('Invalid token header. No credentials provided.')
            self.msg["isSuccess"] = False
            raise AuthenticationError(self.msg)
        elif len(auth) > 2:
            self.msg["message"] = _('Invalid token header. Token string should not contain spaces.')
            self.msg["isSuccess"] = False
            raise AuthenticationError(self.msg)

        try:
            token = auth[1].decode()
        except UnicodeError:
            self.msg["message"] = _('Invalid token header.'
                                    ' Token string should not contain invalid characters.')
            self.msg["isSuccess"] = False
            raise AuthenticationError(self.msg)

        return self.authenticate_credentials(token)
