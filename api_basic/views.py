from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Articale
from .serializers import ArticaleSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.shortcuts import get_object_or_404



# Create your views here.

# class ArticaleViewSet(viewsets.ViewSet):
#     def list(self, request):
#         articales = Articale.objects.all()
#         serializer = ArticaleSerializer(articales, many=True)
#         return Response(serializer.data)
#
#     def create(self, request):
#         serializer = ArticaleSerializer(data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def retrieve(self, request, pk=None):
#         queryset = Articale.objects.all()
#         articale = get_object_or_404(queryset, pk=pk)
#         serializer = ArticaleSerializer(articale)
#         return Response(serializer.data)
#
#     def update(self, request, pk=None):
#         articale = Articale.objects.get(pk=pk)
#         serializer = ArticaleSerializer(articale, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self,request, pk=None):
#         articale = Articale.objects.get(pk=pk)
#         articale.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class ArticaleViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,
#                       mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
#     serializer_class = ArticaleSerializer
#     queryset = Articale.objects.all()

class ArticaleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticaleSerializer
    queryset = Articale.objects.all()



class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                     mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = ArticaleSerializer
    queryset = Articale.objects.all()
    lookup_field = 'id'
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)

class ArticaleAPIView(APIView):

    def get(self, request):
        articales = Articale.objects.all()
        serializer = ArticaleSerializer(articales, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticaleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticaleDetails(APIView):

    def get_objects(self, id):
        try:
            return Articale.objects.get(id=id)

        except Articale.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        articale = self.get_objects(id)
        serializer = ArticaleSerializer(articale)
        return Response(serializer.data)

    def put(self, request, id):
        articale = self.get_objects(id)
        serializer = ArticaleSerializer(articale, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        articale = self.get_objects(id)
        articale.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def articale_list(request):
    if request.method == 'GET':
        articales = Articale.objects.all()
        serializer = ArticaleSerializer(articales, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticaleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def articale_detail(request, pk):
    try:
        articale = Articale.objects.get(pk=pk)

    except Articale.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticaleSerializer(articale)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArticaleSerializer(articale, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        articale.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
