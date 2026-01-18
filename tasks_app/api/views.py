from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from tasks_app.models import Task

# start Task Views
@api_view(['GET','POST'])
def tasks_view(request):

    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response({"tasks": serializer.data})

    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)