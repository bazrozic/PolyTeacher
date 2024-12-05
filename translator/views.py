from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from translator.models import Translation
from translator.serializers import TranslationSerializer

# Create your views here.

class FrenchSpanishTranslationViewSet(APIView):

    def get(self, request):
        translations = Translation.objects.filter(source_language='FR', target_language='ES')
        print(f'translations: {translations}')
        serializer = TranslationSerializer(translations, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        return Response(data={}, status=None)
    
    def put(self, request, pk):
        return Response(data={}, status=None)
    
    def delete(self, request, pk):
        return Response(data={}, status=None)
    
class FrenchEnglishTranslationViewSet(APIView):

    def get(self, request):
        return Response(data={}, status=None)
    
    def post(self, request):
        return Response(data={}, status=None)
    
    def put(self, request, pk):
        return Response(data={}, status=None)
    
    def delete(self, request, pk):
        return Response(data={}, status=None)

def index(request):
    return render(request, 'index.html', context={})


class AllTranslationsViewSet(APIView):

    def get(self, request):
        translations = Translation.objects.all()
        serializer = TranslationSerializer(translations, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = TranslationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        translation = Translation.objects.get(pk=pk)
        serializer = TranslationSerializer(translation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        translation = Translation.objects.get(pk=pk)
        translation.delete()
        return Response(data={}, status=status.HTTP_204_NO_CONTENT)