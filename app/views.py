from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from app.serializers import URLSerializer
import string, random,json,io
from app.models import Short
# Create your views here.
def abc(request):
    return HttpResponse("<h1>Url Shortener</h1>")
class EmployeeList(APIView):
    def get(self,request,*args,**kwargs):
        qs=Short.objects.all().values_list('shortcode')
        b=list(qs)
        for z in b:
            for y in z:
                if request.data.get('shortcode') == y:return Response({'msg':'Shortcode Exists'},status=302)
                else:return Response({'msg':'Shortcode Not Exists'},status=404)
    def post(self,request,*args,**kwargs):
        qs=Short.objects.all().values_list('shortcode')
        b=list(qs)
        for z in b:
            for y in z:
                if request.data.get('shortcode') == y:return Response({'msg':'Shortcode is Already in Use'},status=409)
                else:
                    if request.data.get('url') is None:
                        return Response({'message':'URL Not Present'},status=400)
                    elif request.data.get('shortcode').isalpha() or len(request.data.get('shortcode'))<=5 or request.data.get('shortcode').isdigit():
                        return Response({'message':'Short is Not Valid'},status=412)
                    else:
                        if request.data.get('shortcode') is None:
                            s1 = string.ascii_uppercase + string.ascii_lowercase+'_'
                            s2=string.digits
                            url_id1 = ''.join(random.choices(s1, k=3))
                            url_id2 = ''.join(random.choices(s2, k=3))
                            data=url_id1+url_id2
                        else:data=request.data.get('shortcode')
                        s=Short(url=request.data.get('url'),shortcode=data)
                        s.save()
                        return Response({'shortcode':data},status=201)
