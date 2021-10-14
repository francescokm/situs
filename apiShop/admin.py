from django.contrib import admin
from .models import Kategori, Produk, Harga

class KategoriAdmin(admin.ModelAdmin):
    list_display = ("nama", "gambar1","gambar2","gambar3","deskripsi",)

class ProdukAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Produk._meta.fields]
    exclude = ('created', 'modified','id',)

class HargaAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Harga._meta.fields]
    exclude = ('created', 'modified','id',)

    

admin.site.register(Kategori, KategoriAdmin)
admin.site.register(Produk, ProdukAdmin)
admin.site.register(Harga, HargaAdmin)

