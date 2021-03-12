from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from .models import Driver,Advertiser
from .serializers import DriverSerializer,AdvertiserSerialiser

class GetDrivers(APIView):
    def get(self, request, pk):
        """ Geting all Drivers """
        Drivers = get_object_or_404(Driver.objects.all(), pk = pk)
        serializer = DriverSerializer(Drivers)
        return Response({'Drivers': serializer.data})

    def post(self, request):
        serialiser = DriverSerializer(data = Driver)
        if serialiser.is_valid(rise_exeption = True):
            Driver_saved = serialiser.save()
        return Response({'success': "Driver {} created!".format(Driver_saved.name)})

    def put(self, request, pk):
        Driver_saved = get_object_or_404(Driver.objects.all(), pk = pk)
        data = request.data.get("Driver")
        serializer = DriverSerializer(instance = Driver_saved, data = data, partial = True)

        if serializer.is_valid(raise_exeption = True):
            Driver_saved = serializer.save()
            return Response({"succes":"Updated {}.".format(Driver_saved.name)})
    def delete(self, request, pk):
        Driver = get_object_or_404(Driver.objects.all(), pk = pk)
        Driver.delete()
        return Response({"message":"Driver {} has been deleted.".format(pk)}, status = 204)



class GetAdvertisers(APIView):
    def get(self, request, pk):
        """ Geting all Advertisers """
        Advertisers = get_object_or_404(Advertiser.objects.all(), pk = pk)
        serializer = AdvertiserSerialiser(Advertisers)
        return Response({'Advertisers': serializer.data})

    def post(self, request):
        serialiser = AdvertiserSerialiser(data = Advertiser)
        if serialiser.is_valid(rise_exeption = True):
            Advertiser_saved = serialiser.save()
        return Response({'success': "Advertiser {} created!".format(Advertiser_saved.name)})

    def put(self, request, pk):
        Advertiser_saved = get_object_or_404(Advertiser.objects.all(), pk = pk)
        data = request.data.get("Advertiser")
        serializer = AdvertiserSerialiser(instance = Advertiser_saved, data = data, partial = True)

        if serializer.is_valid(raise_exeption = True):
            Advertiser_saved = serializer.save()
            return Response({"succes":"Updated {}.".format(Advertiser_saved.name)})
    def delete(self, request, pk):
        Advertiser = get_object_or_404(Advertiser.objects.all(), pk = pk)
        Advertiser.delete()
        return Response({"message":"Advertiser {} has been deleted.".format(pk)}, status = 204)


