from rest_framework import serializers
from apiShop.models import Kategori as M_Kategori, Keranjang, Produk as M_Produk, Harga as M_Harga
from apiShop.models import Provinsi, Kabupaten, Kecamatan, CustomUser as M_User





class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = M_User
        fields = ('first_name', 'last_name', 'email', 'hp','username', 'password','is_customer')

    def create(self, validated_data):
        user = super(CustomUserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

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

class KecamatanSerial(serializers.ModelSerializer):    
    class Meta :
        model = Kecamatan
        fields = '__all__'
        read_only_fields = ('id',)

class KabupatenSerial(serializers.ModelSerializer):
    
    class Meta :
        model = Kabupaten
        fields = '__all__'
        read_only_fields = ('id',)


class ProvinsiSerial(serializers.ModelSerializer):
    
    class Meta :
        model = Provinsi
        fields = '__all__'
        read_only_fields = ('id',)


class KeranjangSerial(serializers.ModelSerializer):
    harga = HargaSerial(many=True, read_only=True)
    class Meta :
        model = Keranjang
        read_only_fields = ('id',)
        exclude = ('created', 'modified',)

