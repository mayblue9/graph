from random import randint

from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.authentication import SessionAuthentication
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser
from rest_framework.parsers import FormParser
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from rest_framework.response import Response

from app.settings import MEDIA_ROOT
from .models import Cam


def index(request):
    #graphs = Graph.objects.order_by('-pk')    
    context = {'content': ''}
    return render(request, 'sandbox/index.html', context)


class CamFileUpload(APIView):
    parser_classes = (MultiPartParser, FormParser,)
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    """
    def get(self, request, format=None):
        content = {
            'user': unicode(request.user),  # `django.contrib.auth.User` instance.
            'auth': unicode(request.auth),  # None
        }
        return Response(content)
    """

    def put(self, request, format=None):
        #print('\n---\n')
        #print('\n---\n',request.data['csrfmiddlewaretoken'],'\n---\n')

        file_obj = request.data['zfile']
        camID = request.data['camID']

        cam = Cam.objects.get(pk=camID)
        cam.fileData = file_obj
        #cam.save(using='sandbox')
        cam.save()

        """
        destination = open(MEDIA_ROOT + '/' + str(randint(0,9999)) + '_' + file_obj.name, 'wb+')
        for chunk in file_obj.chunks():
            destination.write(chunk)
        destination.close()
        """

        return Response(status=200)


