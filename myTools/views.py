from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView
from .models import Tool
from .serializers import ToolSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


class homePageView(TemplateView):
    template_name = "home.html"


@api_view(['GET', 'POST'])
def tool_list(request, format=None):
    if request.method == 'GET':
        tools = Tool.objects.all()
        serializer = ToolSerializer(tools, many=True)
        return Response(serializer.data)
        # return JsonResponse({'Tools': serializer.data})

    if request.method == 'POST':
        serializer = ToolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def tool_detail(request, id, format=None):

    try:
        tool = Tool.objects.get(pk=id)
    except Tool.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ToolSerializer(tool)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ToolSerializer(tool, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        tool.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)