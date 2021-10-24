from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Kategori as M_Kategori, Produk as M_Produk
from .models import Keranjang as M_Keranjang
from .models import Provinsi as M_Provinsi
from .models import Kabupaten as M_Kab
from .models import Kecamatan as M_Kec
from .models import CustomUser as M_User
from .models import Harga as M_Harga

from .serializers import KategoriSerial, ProdukSerial, KeranjangSerial, CustomUserSerializer
from .serializers import ProvinsiSerial, KabupatenSerial, KecamatanSerial, HargaSerial
from rest_framework.permissions import BasePermission, AllowAny,IsAuthenticated, SAFE_METHODS
from rest_framework.decorators import permission_classes


class RegisterUser(generics.CreateAPIView):
  serializer_class = CustomUserSerializer
  query_set = M_User.objects.all()
  

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class KategoriAPIView(APIView):
    permission_classes = [IsAuthenticated|ReadOnly]
    
    def get(self, request, format=None):
        dataKategori = M_Kategori.objects.all()
        serializer = KategoriSerial(dataKategori, many=True)
        return Response(serializer.data)

    
    def post(self, request, format=None):
        serializer = KategoriSerial(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class KategoriDetail(APIView):
    permission_classes = [IsAuthenticated|ReadOnly]

    def get_object(self, pk):
        try:
            return M_Kategori.objects.get(pk=pk)
        except M_Kategori.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        dataKategori = self.get_object(pk)
        serializer = KategoriSerial(dataKategori)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        dataKategori = self.get_object(pk)
        serializer = KategoriSerial(dataKategori, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        dataKategori = self.get_object(pk)
        dataKategori.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProdukAPIView(APIView):
    permission_classes = [IsAuthenticated|ReadOnly]
    
    def get(self, request, format=None):
        dataProduk = M_Produk.objects.all()
        serializer = ProdukSerial(dataProduk, many=True)
        return Response(serializer.data)

    
    # def post(self, request, format=None):
    #     serializer = ProdukSerial(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProdukDetail(APIView):
    permission_classes = [IsAuthenticated|ReadOnly]

    def get_object(self, pk):
        try:
            return M_Produk.objects.get(pk=pk)
        except M_Produk.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        dataProduk = self.get_object(pk)
        serializer = ProdukSerial(dataProduk)
        return Response(serializer.data)

    def get_queryset(self):
        kategori = self.request.query_params.get('kategori')        
        try:
            return M_Produk.objects.filter(kategori=kategori)
        except M_Produk.DoesNotExist:
            raise Http404
    # def put(self, request, pk, format=None):
    #     dataProduk = self.get_object(pk)
    #     serializer = ProdukSerial(dataProduk, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def delete(self, request, pk, format=None):
    #     dataProduk = self.get_object(pk)
    #     dataProduk.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

class KecamatanDetail(generics.ListAPIView):
    permission_classes = [AllowAny]       

    model = M_Kec
    serializer_class = KecamatanSerial
    def get_queryset(self):
        pk = self.kwargs['pk']
        try:
            return M_Kec.objects.filter(kabupaten=pk)
        except M_Kec.DoesNotExist:
            raise Http404

class KabupatenDetail(generics.ListAPIView):
    permission_classes = [AllowAny]
    
    model = M_Kab
    serializer_class = KabupatenSerial
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        try:
            return M_Kab.objects.filter(provinsi=pk)
        except M_Kab.DoesNotExist:
            raise Http404

class ProvinsiAPIView(APIView):
    permission_classes = [ReadOnly]
    
    def get(self, request, format=None):
        dataProv = M_Provinsi.objects.all()
        serializer = ProvinsiSerial(dataProv, many=True)
        return Response(serializer.data)

class KeranjangAPIView(APIView):
    permission_classes = [IsAuthenticated|ReadOnly]
    
    def get(self, request, format=None):
        dataKeranjang = M_Keranjang.objects.all()
        serializer = KeranjangSerial(dataKeranjang, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = KeranjangSerial(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class KeranjangUserDetail(generics.ListAPIView):
    permission_classes = [AllowAny]
    
    model = M_Keranjang
    serializer_class = KeranjangSerial
    
    def get_queryset(self):
        user = self.kwargs['user']
        try:
            return M_Keranjang.objects.filter(user=user)
        except M_Keranjang.DoesNotExist:
            raise Http404

class KeranjangDetail(APIView):
    permission_classes = [IsAuthenticated|ReadOnly]

    def get_object(self, pk):
        try:
            return M_Keranjang.objects.get(pk=pk)
        except M_Keranjang.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        dataKeranjang = self.get_object(pk)
        serializer = KeranjangSerial(dataKeranjang)
        return Response(serializer.data)

    
    def put(self, request, pk, format=None):
        dataProduk = self.get_object(pk)
        serializer = ProdukSerial(dataProduk, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        dataProduk = self.get_object(pk)
        dataProduk.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class HargaDetail(generics.ListAPIView):
    permission_classes = [AllowAny]
    
    model = M_Harga
    serializer_class = HargaSerial
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        try:
            return M_Harga.objects.filter(produk=pk)
        except M_Harga.DoesNotExist:
            raise Http404

