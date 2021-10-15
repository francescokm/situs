from django.db import models
from django.contrib.auth.models import User as M_User
from django.db.models.base import Model
from cloudinary.models import CloudinaryField


class Provinsi(models.Model):
    nama = models.CharField(max_length=175)

    def __str__(self):
        return str('%s' % (self.nama))
    
    class Meta:
        verbose_name_plural = "API Provinsi"


class Kabupaten(models.Model):
    nama = models.CharField(max_length=175)
    provinsi = models.ForeignKey(Provinsi, related_name='kabupaten', on_delete=models.CASCADE)

    def __str__(self):
        return str('%s' % (self.nama))
    
    class Meta:
        verbose_name_plural = "API Kabupaten & Kota"

class Kecamatan(models.Model):
    nama = models.CharField(max_length=175)
    kabupaten = models.ForeignKey(Kabupaten, related_name='kecamatan', on_delete=models.CASCADE)

    def __str__(self):
        return str('%s' % (self.nama))
    
    class Meta:
        verbose_name_plural = "API Kecamatan"



class Alamat(models.Model):
    user = models.OneToOneField(M_User, on_delete=models.CASCADE)
    jalan = models.TextField()
    jalan_tambahan = models.TextField(null=True, blank=True) 
    kecamatan = models.OneToOneField(Kecamatan, on_delete=models.CASCADE)
    kabupaten = models.OneToOneField(Kabupaten, on_delete=models.CASCADE)
    provinsi = models.OneToOneField(Provinsi, on_delete=models.CASCADE)
    kodePos = models.CharField(max_length=5)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now_add=True)

    def __str__(self):
        return str('%s' % (self.jalan))
    
    class Meta:
        verbose_name_plural = "API Alamat Utama Client"


class AlamatTambahan(models.Model):
    user = models.ForeignKey(M_User, related_name='alamatTambahan', on_delete=models.CASCADE)
    jalan = models.TextField()
    jalan_tambahan = models.TextField(null=True, blank=True) 
    kecamatan = models.OneToOneField(Kecamatan, on_delete=models.CASCADE)
    kabupaten = models.OneToOneField(Kabupaten, on_delete=models.CASCADE)
    provinsi = models.OneToOneField(Provinsi, on_delete=models.CASCADE)
    kodePos = models.CharField(max_length=5)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now_add=True)

    def __str__(self):
        return str('%s' % (self.jalan))
    
    class Meta:
        verbose_name_plural = "API Alamat Lain Client"


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


class Keranjang(models.Model):
    user = models.ForeignKey(M_User, related_name='keranjang', on_delete=models.CASCADE)
    produk = models.ForeignKey(Produk, related_name='keranjang', on_delete=models.CASCADE)
    qty = models.IntegerField()     
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now_add=True)
    

    class Meta:
        verbose_name_plural = "API Kerangjang Client"