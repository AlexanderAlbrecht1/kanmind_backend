from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET','POST'])
def single_board_view(request):
    if request.method == 'GET':
        return Response({"message": "This is a GET request"})
    if request.method == 'POST':
        try:
            data = request.data # hier kommt hin in welchem format die daten eingegebn werden müssen
            return Response({"new_board_added": data}, status=201)
        except:
            return Response({"error": "Invalid data"}, status=400)