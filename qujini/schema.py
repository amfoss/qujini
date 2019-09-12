import graphene
import questions.schema 


class Query(questions.schema.Query, graphene.ObjectType):
        # This class extends all abstract apps level Queries and graphene.ObjectType
        pass

schema = graphene.Schema(query=Query)
