from rest_framework import serializers
from apiShop.models import Kategori as M_Kategori

class KategoriSerial(serializers.ModelSerializer):

    class Meta :
        model = M_Kategori
        fields = ['id','nama','gambar1','gambar2','gambar3']
        read_only_fields = ('id',)