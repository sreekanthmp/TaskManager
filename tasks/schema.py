import graphene
from graphene_django import DjangoObjectType
from tasks.models import Task
from graphql import GraphQLError


class TaskType(DjangoObjectType):
    class Meta:
        model = Task


class Query(graphene.ObjectType):
    tasks = graphene.List(TaskType)
    task = graphene.Field(TaskType, id=graphene.Int())

    def resolve_tasks(self, info, **kwargs):
        user = info.context.user

        if not user.is_authenticated:
            raise GraphQLError('You must be logged in to view tasks!')
        return Task.objects.all()

    def resolve_task(self, info, id):
        user = info.context.user

        if not user.is_authenticated:
            raise GraphQLError('You must be logged in to view tasks!')
        return Task.objects.filter(assigned_to=user, id=id).first()


class CreateTask(graphene.Mutation):
    task = graphene.Field(TaskType)

    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String()
        status = graphene.String()

    def mutate(self, info, title, description=None, status=None):
        user = info.context.user

        if not user.is_authenticated:
            raise GraphQLError('You must be logged in to create tasks!')

        task = Task(
            title=title,
            description=description,
            status=status or 'TODO',
            assigned_to=user
        )
        task.save()
        return CreateTask(task=task)


class Mutation(graphene.ObjectType):
    create_task = CreateTask.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
