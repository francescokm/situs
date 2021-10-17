from django.contrib import admin
from django.db import models
from .models import Kategori, Produk, Harga, Alamat, AlamatTambahan, CustomUser, Keranjang
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Customer',
            {
                'fields':(
                    'hp',
                    'is_customer',
                )
            }
        )
    )


class KategoriAdmin(admin.ModelAdmin):
    list_display = ("nama", "gambar1","gambar2","gambar3","deskripsi",)

class ProdukAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Produk._meta.fields]
    exclude = ('created', 'modified','id',)

class HargaAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Harga._meta.fields]
    exclude = ('created', 'modified','id',)

class KeranjangAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Keranjang._meta.fields]
    exclude = ('created', 'modified','id',)


class AlamatInline(admin.StackedInline):
    model = Alamat
    can_delete = False
    verbose_name_plural = 'Alamat Client'

class AlamatTambahanInline(admin.StackedInline):
    model = AlamatTambahan
    can_delete = False
    verbose_name_plural = 'Alamat Tambahan Client'



admin.site.register(Kategori, KategoriAdmin)
admin.site.register(Produk, ProdukAdmin)
admin.site.register(Harga, HargaAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Keranjang, KeranjangAdmin)

