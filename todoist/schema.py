import graphene
from graphene_django import DjangoObjectType
from userapp.models import User
from todoapp.models import Project, ToDo


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class ToDoType(DjangoObjectType):
    class Meta:
        model = ToDo
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    all_todos = graphene.List(ToDoType)
    all_projects = graphene.List(ProjectType)
    project_todos = graphene.List(ToDoType, project=graphene.Int(required=True))
    project_members = graphene.List(UserType, project=graphene.Int(required=True))
    todo_by_text = graphene.List(ToDoType, text=graphene.String())

    def resolve_all_users(self, info):
        return User.objects.all()

    def resolve_all_todos(self, info):
        return ToDo.objects.all()

    def resolve_all_projects(self, info):
        return Project.objects.all()

    def resolve_project_todos(self, info, project):
        return ToDo.objects.filter(project=project)

    def resolve_project_members(self, info, project):
        return Project.objects.filter(id=project).first().members.all()

    def resolve_todo_by_text(self, info, text):
        return ToDo.objects.filter(text__contains=text)


schema = graphene.Schema(query=Query)
