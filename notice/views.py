from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from .models import Deadlines,Users
import datetime

@api_view(['GET','POST','DELETE','PUT'])
def getDocs(request):
    print(Deadlines.objects.all().values())
    return Response(Deadlines.objects.all().values())
def getDay(request):
    if request.method=="GET":
        uid=request.body['id']
        queryset=Users.objects.get(user_id=uid)

        dl_queryset=Deadlines.objects.get(dl_id=queryset.deadline)

        start=datetime.datetime(dl_queryset.startdate)
        end=datetime.datetime(dl_queryset.enddate)
        day=(end-start).days

        startday=(datetime.datetime.now()-start).days
        endday=(end-datetime.datetime.now()).days

        if day-endday==3:
            return Response({'notice':'yellow'})
        elif day-endday==1:
            return Response({'notice':'red'})



