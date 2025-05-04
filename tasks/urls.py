from django.urls import path
from tasks.schema import schema
from tasks.views.graphql_auth import GraphQLModelView  
from .views.token_auth import CustomAuthToken
from .views.tasks import TaskModelViewSet


urlpatterns = [
    path('api/login', CustomAuthToken.as_view(), name='api-token'),
    path('api/task', TaskModelViewSet.as_view(
        {'get': 'list', 'post': 'create'}), name='task-list-create'),
    path('api/task/<int:pk>', TaskModelViewSet.as_view(
        {'put': 'update', 'delete': 'destroy'}), name='task-update-delete'),
    path("graphql", GraphQLModelView.as_view(graphiql=True, 
                                                      schema=schema)),
]