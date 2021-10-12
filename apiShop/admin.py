from django.contrib import admin
from .models import Kategori

class KategoriAdmin(admin.ModelAdmin):
    list_display = ("nama", "gambar1","gambar2","gambar3","deskripsi",)


admin.site.register(Kategori, KategoriAdmin)
