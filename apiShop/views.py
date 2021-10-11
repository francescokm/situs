from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import Kategori as M_Kategori
from .serializers import KategoriSerial


class KategoriAPIView(ListAPIView):
    permission_classes = (AllowAny,)
    queryset = M_Kategori.objects.all()
    serializer_class = KategoriSerial

class CreateKategoriAPIView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = M_Kategori.objects.all()
    serializer_class = KategoriSerial

class UpdateKategoriAPIView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = M_Kategori.objects.all()
    serializer_class = KategoriSerial

class DeleteKategoriAPIView(DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = M_Kategori.objects.all()
    serializer_class = KategoriSerial