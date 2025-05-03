from rest_framework import viewsets
from common.views.authenticated_view import AuthenticatedView
from common.utils.pagination import CustomPageNumberPagination


class PaginatedAuthView(AuthenticatedView):
    """ Base class for the views which needs to be paginated. """
    pagination_class = CustomPageNumberPagination

    def __init__(self, *args, **kwargs):
        super(PaginatedAuthView, self).__init__(*args, **kwargs)


class PaginatedAuthViewSet(PaginatedAuthView, viewsets.ViewSet):
    """Base class for the views which needs to be paginated in application"""
    pass


class PaginatedAuthModelViewSet(PaginatedAuthView, viewsets.ModelViewSet):
    """Base class for the views which needs to be paginated in application"""
    pass
