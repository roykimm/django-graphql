import graphene
from graphene_django import DjangoObjectType, DjangoListField
from .models import Quizzes, Category, Question, Answer

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name")

class QuizzesType(DjangoObjectType):
    class Meta:
        model = Quizzes
        fields = ("id", "title", "category")

class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fiels = ("title", "quiz")

class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ("question", "answer_text")

class Query(graphene.ObjectType):

    # quiz = graphene.String()

    # def resolve_quiz(root, info):
    #     return f"This is the first question"

    #all_quizzes = DjangoListField(QuizzesType)
    all_questions = graphene.Field(QuestionType, id=graphene.Int())
    all_answers = graphene.List(AnswerType, id=graphene.Int())

    #all_questions = graphene.List(QuestionType)
    #all_questions = DjangoListField(QuestionType)
    
    def resolve_all_questions(root,info,id):
        #return Quizzes.objects.all()
        #return Quizzes.objects.filter(id=1)
        return Question.objects.get(pk=id)
    
    def resolve_all_answers(root,info,id):
        #return Quizzes.objects.all()
        #return Quizzes.objects.filter(id=1)
        return Answer.objects.filter(question=id)

# class CategoryMutation(graphene.Mutation):

#     class Arguments:
#         name = graphene.String(required=True)

#     category = graphene.Field(CategoryType)

#     @classmethod
#     def mutate(cls, root, info, name):
#         category = Category(name=name)
#         category.save()
#         return CategoryMutation(category=category)

class CategoryMutation(graphene.Mutation):

    class Arguments :
        id = graphene.ID()
        #name  = graphene.String(required=True)

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, id):
        category = Category.objects.get(id=id)
        #category.name = name
        #category.save()
        category.delete()
        #return CategoryMutation(category=category)
        return

class Mutation(graphene.ObjectType):

    update_category = CategoryMutation.Field()
    

schema = graphene.Schema(query=Query, mutation=Mutation)