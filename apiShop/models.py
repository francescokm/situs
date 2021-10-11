from django.db import models
from cloudinary.models import CloudinaryField

class Kategori(models.Model):
    nama = models.CharField(max_length=75)
    gambar1 =  CloudinaryField('gambar1')
    gambar2 =  CloudinaryField('gambar2', null=True, blank=True)
    gambar3 =  CloudinaryField('gambar3', null=True, blank=True)
        
    
    def __str__(self):
        return str('%s' % (self.nama))
    
    class Meta:
        verbose_name_plural = "API Kategori"