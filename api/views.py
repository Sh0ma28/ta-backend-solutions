from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Status, Type, Category, Subcategory, Record
from .serializers import StatusSerializer, TypeSerializer, CategorySerializer, SubcategorySerializer, RecordSerializer

# API Routes
@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/statuses/',
            'method': ['GET', 'POST'],
            'body': {
                'name': 'string'
            }
        },
        {
            'Endpoint': '/statuses/id',
            'method': ['GET', 'PUT', 'DELETE'],
            'body': {
                'name': 'string'
            }
        },
        {
            'Endpoint': '/types/',
            'method': ['GET', 'POST'],
            'body': {
                'name': 'string'
            }
        },
        {
            'Endpoint': '/types/id',
            'method': ['GET', 'PUT', 'DELETE'],
            'body': {
                'name': 'string'
            }
        },
        {
            'Endpoint': '/categories/',
            'method': ['GET', 'POST'],
            'body': {
                'name': 'string',
                'type': 'url'
            }
        },
        {
            'Endpoint': '/categories/id',
            'method': ['GET', 'PUT', 'DELETE'],
            'body': {
                'name': 'string',
                'type': 'url'
            }
        },
        {
            'Endpoint': '/subcategories/',
            'method': ['GET', 'POST'],
            'body': {
                'name': 'string',
                'category': 'url'
            }
        },
        {
            'Endpoint': '/subcategories/id',
            'method': ['GET', 'PUT', 'DELETE'],
            'body': {
                'name': 'string',
                'category': 'url'
            }
        },
        {
            'Endpoint': '/records/',
            'method': ['GET', 'POST'],
            'body': {
                'status': 'string',
                'subcategory': 'url',
                'value': 'id',
                'comment': 'string',
            }
        },
        {
            'Endpoint': '/records/id',
            'method': ['GET', 'PUT', 'DELETE'],
            'body': {
                'created_at': 'date',
                'status': 'string',
                'subcategory': 'url',
                'value': 'id',
                'comment': 'string',
            }
        },
    ]
    return Response(routes)

# Status views
class StatusListCreate(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class StatusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

# Type views
class TypeListCreate(generics.ListCreateAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

class TypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

# Category views
class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Subcategory views
class SubcategoryListCreate(generics.ListCreateAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer

class SubcategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer

# Record views
class RecordListCreate(generics.ListCreateAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

class RecordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
