from django.urls import path
from apiShop.views import KategoriAPIView,KategoriDetail,ProdukAPIView,ProdukDetail
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("kategori",KategoriAPIView.as_view(),name="kategori_list"),
    path("kategori/<int:pk>/",KategoriDetail.as_view(),name="detail_kategori"),
    path("produk",ProdukAPIView.as_view(),name="produk_list"),
    path("produk/<int:pk>/",ProdukDetail.as_view(),name="detail_produk"),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html', 'api'])