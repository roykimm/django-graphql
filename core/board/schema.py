import graphene
from graphene_django.types import DjangoObjectType
from .models import Board

class BoardType(DjangoObjectType):
    class Meta:
        model = Board
        fields = ('no','title','note','writer','count','insert_date','update_date','usage_flag')


class BoardQuery(graphene.ObjectType):
    Boards_all = graphene.List(BoardType)
    Boards_detail = graphene.Field(
        BoardType, b_no=graphene.Int(required=True))

    def resolve_Boards_all(root, info, **kwargs):
        return Board.objects.filter(usage_flag='1')

    def resolve_Boards_detail(self, info, b_no):
        return Board.objects.get(b_no=b_no)


class BoardCreate(graphene.Mutation):

    class Arguments:
        bTitle = graphene.String()
        bWriter = graphene.String()
        bNote = graphene.String()

    boards = graphene.Field(BoardType)

    def mutate(self, info, bTitle, bWriter, bNote):
        boards = Boards.objects.create(
            b_title=bTitle, b_writer=bWriter, b_note=bNote)

        return BoardCreate(boards=boards)


class BoardDelete(graphene.Mutation):

    class Arguments:
        bNo = graphene.Int()

    boards = graphene.Field(BoardType)

    def mutate(self, info, bNo):
        boards = Board.objects.get(b_no=bNo)
        boards.usage_flag = '0'
        boards.save()
        return BoardDelete(boards=boards)


class BoardUpdate(graphene.Mutation):

    class Arguments:
        bNo = graphene.Int()
        bTitle = graphene.String()
        bWriter = graphene.String()
        bNote = graphene.String()

    boards = graphene.Field(BoardType)

    def mutate(Self, info, bNo, bTitle, bWriter, bNote):

        boards = Board.objects.get(b_no=bNo)
        boards.b_title = bTitle
        boards.b_writer = bWriter
        boards.b_note = bNote
        boards.save()
        return BoardUpdate(boards=boards)