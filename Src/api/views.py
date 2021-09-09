from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Secret
from .serializers import SecretSerializer
from django.utils.crypto import get_random_string
from datetime import datetime
from datetime import timedelta
import pytz

# Create your views here.
@api_view(['POST'])
def addSecret(request):
    _hash = get_random_string(length=6)
    secretText = request.data['secretText']
    createdAt = datetime.now()
    expireAfterViews = request.data['expireAfterViews']
    expireAfter = request.data['expireAfter']   #hours
    expiresAt = createdAt + timedelta(hours=int(expireAfter))
    secret = Secret(_hash=_hash, secretText=secretText, createdAt=createdAt, remainingViews=expireAfterViews, expiresAt=expiresAt)
    secret.save()
    return Response({'hash' : 'valami'})



@api_view(['GET']) 
def getSecret(request, _hash):
    try:
        secret = Secret.objects.get(_hash=_hash)
        utc=pytz.UTC
        now = datetime.now().replace(tzinfo=utc)
        if secret.remainingViews != 0 and secret.expiresAt.replace(tzinfo=utc) > now:
            secret.remainingViews -=1
            secret.save()
            serialized_secret = SecretSerializer(secret, many=False)
            return Response(serialized_secret.data)
        else:
            return Response({'Message' : 'This secret has expired!'})
    except:
        return Response('Something went wrong. Maybe a bad hash?')
