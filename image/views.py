from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Image
from .serializers import ImageSerializer
from django.http import JsonResponse

class ImageViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]

    
# Create your views here.
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        images = Image.objects.filter(user = request.user.id)
        print(images)
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
  
    def post(self, request, *args, **kwargs):

        
        wrongData = "Les informations saisies sont incorrectes."
        print(request.user.id, "request.user.id")
        data = {
            'name': request.data.get('name'),
            'tags': request.data.get('tags'),
            'description': request.data.get("description"),
            'base64': request.data.get("base64"),
            'user': request.user.id
        }
           
        serializer = ImageSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)