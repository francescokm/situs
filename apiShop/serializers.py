from rest_framework import serializers
from apiShop.models import Kategori as M_Kategori, Produk as M_Produk, Harga as M_Harga

class KategoriSerial(serializers.ModelSerializer):

    class Meta :
        model = M_Kategori
        fields = ['id','nama','gambar1','gambar2','gambar3', 'deskripsi']
        read_only_fields = ('id',)

class HargaSerial(serializers.ModelSerializer):
    class Meta:
        model = M_Harga
        # fields = '__all__'
        read_only_fields = ('id',)
        exclude = ('created', 'modified',)

class ProdukSerial(serializers.ModelSerializer):
    harga = HargaSerial(many=True, read_only=True)
    class Meta :
        model = M_Produk
        # fields = '__all__'
        read_only_fields = ('id',)
        exclude = ('created', 'modified',)

