# views.py
from graphene_django.views import GraphQLView
from rest_framework.authentication import TokenAuthentication
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from common.views.authenticated_view import AuthenticatedGraphQLView
from rest_framework.exceptions import AuthenticationFailed
from django.http import JsonResponse


class GraphQLModelView(AuthenticatedGraphQLView):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        try:
            for authenticator in self.authentication_classes:
                user_auth_tuple = authenticator().authenticate(request)
                if user_auth_tuple is not None:
                    request.user, _ = user_auth_tuple
                    break
            else:
                request.user = None
        except AuthenticationFailed as e:
            return JsonResponse(
                {"data": {"detail": str(e)}},
                status=401
            )
        return super().dispatch(request, *args, **kwargs)
