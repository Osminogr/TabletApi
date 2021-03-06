from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from .models import MUser
from .serializers import UserSerializer

class GetUsers(APIView):
    def get(self, request, pk):
        """ Geting all users """
        user = get_object_or_404(MUser.objects.all(), pk = pk)
        serializer = UserSerializer(user)
        return Response({'users': serializer.data})

    def post(self, request):
        serialiser = UserSerializer(data = user)
        if serialiser.is_valid(rise_exeption = True):
            user_saved = serialiser.save()
        return Response({'success': "User {} created!".format(user_saved.name)})

    def put(self, request, pk):
        user_saved = get_object_or_404(MUser.objects.all(), pk = pk)
        data = request.data.get("user")
        serializer = UserSerializer(instance = user_saved, data = data, partial = True)

        if serializer.is_valid(raise_exeption = True):
            user_saved = serializer.save()
            return Response({"succes":"Updated {}.".format(user_saved.name)})
    def delete(self, request, pk):
        user = get_object_or_404(MUser.objects.all(), pk = pk)
        user.delete()
        return Response({"message":"User {} has been deleted.".format(pk)}, status = 204)
