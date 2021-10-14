from django.db import models
from cloudinary.models import CloudinaryField

class Kategori(models.Model):
    nama = models.CharField(max_length=75)
    gambar1 =  CloudinaryField('gambar1')
    gambar2 =  CloudinaryField('gambar2', null=True, blank=True)
    gambar3 =  CloudinaryField('gambar3', null=True, blank=True)
    deskripsi = models.TextField(null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return str('%s' % (self.nama))
    
    class Meta:
        verbose_name_plural = "API Kategori"


class Produk(models.Model):
    nama = models.CharField(max_length=75)    
    gambar1 =  CloudinaryField('gambar1')
    gambar2 =  CloudinaryField('gambar2', null=True, blank=True)
    gambar3 =  CloudinaryField('gambar3', null=True, blank=True)
    gambar4 =  CloudinaryField('gambar4', null=True, blank=True)
    gambar5 =  CloudinaryField('gambar5', null=True, blank=True)
    gambar6 =  CloudinaryField('gambar6', null=True, blank=True)
    gambar7 =  CloudinaryField('gambar7', null=True, blank=True)
    gambar8 =  CloudinaryField('gambar8', null=True, blank=True)
    deskripsi = models.TextField(null=True, blank=True)
    spesifikasi = models.TextField(null=True, blank=True)
    kategori = models.ForeignKey(Kategori, related_name='produk', on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now_add=True)

    
    def __str__(self):
        return str('%s' % (self.nama))
    
    class Meta:
        verbose_name_plural = "API Produk"


class Harga(models.Model):    
    produk = models.ForeignKey(Produk, related_name='harga', on_delete=models.CASCADE)
    hargaAwal = models.IntegerField()
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    tanggalAktif = models.DateField()
    jamAktif = models.TimeField()
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now_add=True)
    

    class Meta:
        verbose_name_plural = "API Harga Produk"