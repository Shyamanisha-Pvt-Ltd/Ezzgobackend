from rest_framework.views import APIView
from django.contrib.gis.geos import fromstr, Point
from django.contrib.gis.measure import D
from django.contrib.gis.db.models.functions import Distance
from .models import Shop
from django.http import HttpResponse
from django.core.serializers import serialize

class Home(APIView):
    def get(self, request):
        radius = request.data['radius']
        longitude = request.data['longitude']
        latitude = request.data['latitude']
        user_location = Point(longitude, latitude, srid=4326)
        queryset = Shop.objects.annotate(distance=Distance('location', user_location)).filter(distance__lt = D(km=radius).km * 1000).order_by('distance')
        data = serialize("json", queryset)
        return HttpResponse(data, content_type="application/json")
    
    def post(self, request):
        name = request.data['name']
        latitude = request.data['latitude']
        longitude = request.data['longitude']
        location = Point(longitude, latitude, srid=4326)
        address = request.data['address']
        city = request.data['city']
        modeldata = Shop.objects.create(name=name, location = location, address=address, city=city)
        return HttpResponse(modeldata, content_type="application/json")
    
