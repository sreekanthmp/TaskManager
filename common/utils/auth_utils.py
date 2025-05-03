from rest_framework import HTTP_HEADER_ENCODING


def get_authorization_header(request):
    """
    Return request's 'Authorization:' header, as a bytestring.
    Hide some test client ickyness where the header can be unicode.
    """
    auth = request.META.get('HTTP_AUTHORIZATION', b'')
    if not auth:
        auth = request.GET.get('token', "")
        if auth:
            auth = 'Token ' + auth
    if isinstance(auth, type('')):
        # Work around Django test client oddness
        auth = auth.encode(HTTP_HEADER_ENCODING)
    return auth
