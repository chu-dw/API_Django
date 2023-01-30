from rest_framework import status
from rest_framework.response import response
from rest_framework.views import APIView
from rest_framework import viewsets

from .models import Todo
from .serializers import TodoSimpleSerializer

# Create your views here.
class TodosAPIView(APIView):
    def get(self, request):
        todos = Todo.objects.filter(complete=True)
        serializer = TodoSimpleSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)