import json
import hashlib

from rest_framework.decorators import api_view,permission_classes

from rest_framework.response import Response

from .models import Users

from django.views.decorators.http import require_http_methods
#import sys
#sys.path.insert(0, '../authNew')
#from authNew import authNew






@api_view(['POST'])
@require_http_methods(["POST"])

def signin(request):

    if request.method == 'POST':

        print(request.body.decode('utf-8'))

        raw_data = request.body
        body_unicode = raw_data.decode('utf-8')
        body=json.loads(body_unicode)

        username = body['login']
        password = body['password']

        try:
            queryset = Users.objects.get(login=username,password=hashlib.md5(password.encode('utf')).hexdigest())
            return Response({queryset.is_admin, queryset.login, queryset.user_id,queryset.deadline})
        except:
            return Response("Error")

@api_view(['GET'])
@require_http_methods(["GET"])
# Create your views here.
def logout(request):
    if request.method=='GET':
        return Response({"logout"})