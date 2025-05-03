from common.views.authenticated_view import AuthenticatedModelViewSet
from tasks.models import Task
from tasks.serializers import TaskSerializer
from rest_framework.response import Response
from common.utils.pagination import CustomPageNumberPagination


class TaskModelViewSet(AuthenticatedModelViewSet):
    serializer_class = TaskSerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        return Task.objects.filter(assigned_to=self.request.user)

    def perform_create(self, serializer):
        serializer.save(assigned_to=self.request.user)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
