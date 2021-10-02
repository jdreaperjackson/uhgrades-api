from rest_framework import generics
from rest_framework.views import APIView
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Grade
from .serializers import GradeSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework import filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

def index(request):
    return render(request,'index.html')

@csrf_exempt
def grade_list(request):

    if request.method == 'GET':
        grades = Grade.objects.all()
        serializer = GradeSerializer(grades, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        #CHECK THIS LINE IF ERROR
        serializer = GradeSerializer(data=data, many=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def grade_info(request, pk):
    try:
        grade = Grade.objects.get(pk=pk)

    except Grade.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = GradeSerializer(grade)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = GradeSerializer(grade, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        grade.delete()
        return HttpResponse(status=204)

class GradeListfilter(generics.ListAPIView):

    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['@courseDescription', '@instructorLast']

    # '^' Starts-with search.
    # '=' Exact matches.
    # '@' Full-text search. (Currently only supported Django's PostgreSQL backend.)
    # '$' Regex search.


