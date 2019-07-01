import graphene
from graphene_django.types import DjangoObjectType
from .models import Type, Topic

class TypeNode(DjangoObjectType):
  class Meta:
     model= Type

class TopicNode(DjangoObjectType):
  class Meta:
     model= Topic 

# Writing an app level query
class Query(graphene.ObjectType):
    all_types= graphene.List(TypeNode)
    all_topics= graphene.List(TopicNode)
   
    def resolve_all_types(self, info):
       return Type.objects.all()

    
    def resolve_all_topic(self, info):
       return Topic.objectsall()
