from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BoardSerializer
from main_app.models import Board

@api_view(['GET','POST'])
def boards_view(request):

    if request.method == 'GET':
        boards = Board.objects.all()
        serializer = BoardSerializer(boards, many=True)
        return Response({"boards": serializer.data})

    if request.method == 'POST':
        serializer = BoardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)

@api_view(['GET','DELETE', 'PUT'])
def single_board_view(request, board_id):

    if request.method == 'GET':
        board = Board.objects.get(id=board_id)
        serializer = BoardSerializer(board)
        return Response({"board": serializer.data})
    
    if request.method == 'PUT':
        board = Board.objects.get(id=board_id)
        serializer = BoardSerializer(board, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)

    if request.method == 'DELETE':
        board = Board.objects.get(id=board_id)
        serializer = BoardSerializer(board)
        board.delete()
        return Response({"board": serializer.data})
