"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest
from django.template import RequestContext
from datetime import datetime

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from .models import Input
from .models import Output
from .serializers import InputSerializer
from .serializers import OutputSerializer

import requests
from rest_framework.renderers import JSONRenderer
import psycopg2
import unicodedata
import json, simplejson
from rest_framework.parsers import JSONParser


class Inputs(APIView):

    def get(self, request):
        stocks = Input.objects.all()
        serializer = InputSerializer(stocks, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass
        serializer = InputSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Outputs(APIView):

    def get(self, request):
        stocks1 = Output.objects.all()
        serializer1 = OutputSerializer(stocks1, many=True)
        return Response(serializer1.data)

    def post(self, request):
        pass
        serializer1 = OutputSerializer(data=request.data)
        if serializer1.is_valid():
            serializer1.save()
            return Response(serializer1.data, status=status.HTTP_201_CREATED)
        return Response(serializer1.errors, status=status.HTTP_400_BAD_REQUEST)
"""
    def post(self, request):
        data = {'Value1' : self.request["Value1"]}
        data = json.dumps(data)
        return HttpResponse(data)
"""



def regelung(request):
    if request.user.is_authenticated():
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'Info/regelung.html')


def monitoring(request):
    if request.user.is_authenticated():
        #Renders the home page.
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'Info/monitoring.html',
            {
                'title':'Home Page',
                'year':datetime.now().year,
            }
        )


"""
def IAS_Cloud(request):

    global json_list
    global dbrows

    #assert isinstance(request, HttpRequest)
    Parameter = 'Presskraft'
    #Value_List = [1,2,3]

    args = {'Parameter' : Parameter, 'Value_List' : json_list};
    return render(request, 'Info/login_alt.html', args)
"""


def home(request):
    if request.user.is_authenticated():
        #Renders the home page.
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'Info/home.html',
            {
                'title':'Home Page',
                'year':datetime.now().year,
            }
        )

"""
def home(request):
    #Renders the home page.
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )
"""

def contact(request):
    if request.user.is_authenticated():
        #Renders the contact page.
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'Info/contact.html',
            {
                'title':'Contact',
                'message':'Your contact page.',
                'year':datetime.now().year,
            }
        )

def about(request):
    if request.user.is_authenticated():
        #Renders the about page.
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'Info/about.html',
            {
                'title':'About',
                'message':'Your application description page.',
                'year':datetime.now().year,
            }
        )