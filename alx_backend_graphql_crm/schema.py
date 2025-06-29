import graphene
from crm.schema import Query as CrmQuery, Mutation as CrmMutation

schema = graphene.Schema(
    query=CrmQuery,
    mutation=CrmMutation
)
