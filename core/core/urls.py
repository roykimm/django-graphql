
from django.contrib import admin
from django.urls import path, include
from .schema import schema

from graphene_django.views import GraphQLView

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('graphql/',GraphQLView.as_view(graphiql=True, schema=schema)),
    #path('', include('quiz.urls')),
]
