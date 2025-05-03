from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from common.views.base_view import BaseView
from common.authentication.token_authentication import TokenInQueryAuthentication
from common.custom_renderer import CustomRenderer
from graphene_django.views import GraphQLView


class AuthenticatedView(BaseView):
    """ Base class for the views which needs to be authenticated. """
    authentication_classes = [TokenInQueryAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def __init__(self, *args, **kwargs):
        super(AuthenticatedView, self).__init__(*args, **kwargs)


class AuthenticatedViewSet(AuthenticatedView, viewsets.ViewSet):
    """Base class for the views which needs to be authenticated in application"""
    # renderer_classes = [CustomRenderer, ]
    pass


class AuthenticatedModelViewSet(AuthenticatedView, viewsets.ModelViewSet):
    """Base class for the views which needs to be authenticated in application"""
    pass


class AuthenticatedAPIView(AuthenticatedView, APIView):
    """Base class for the views which needs to be authenticated in application"""
    pass


class AuthenticatedGraphQLView(AuthenticatedView, GraphQLView):
    """Base class for the views which needs to be authenticated in application"""
    pass
