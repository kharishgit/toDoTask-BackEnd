from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task
# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_url = {
        'List':'/taskList',
        'Detail view':'taskDetail/<str:pk>/',
        'Create' :'/taskCreate',
        'Update' :'/taskUpdate/<str:pk>/',
        'Delete' :'/taskDelete/<str:pk>/',
    }
    return Response(api_url)
@api_view(['GET'])
def taskList(request):
    task = Task.objects.all()
    print(task)
    serializer = TaskSerializer(task,many=True)
    print(serializer.data)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request,pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request,pk):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def taskUpdate(request,pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()
    serializer = TaskSerializer(task,many=False)
    return Response(serializer.data)


