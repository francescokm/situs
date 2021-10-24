from django.urls import path
from apiShop.views import KategoriAPIView,KategoriDetail,ProdukAPIView,ProdukDetail
from apiShop.views import KeranjangDetail, ProvinsiAPIView, KabupatenDetail, KecamatanDetail
from apiShop.views import KeranjangAPIView, RegisterUser, HargaDetail, KeranjangUserDetail
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("kategori",KategoriAPIView.as_view(),name="kategori_list"),
    path("kategori/<int:pk>/",KategoriDetail.as_view(),name="detail_kategori"),
    path("produk",ProdukAPIView.as_view(),name="produk_list"),
    path("produk/<int:pk>/",ProdukDetail.as_view(),name="detail_produk"),
    path("provinsi",ProvinsiAPIView.as_view(),name="provinsi_list"),
    path("kabupaten/<int:pk>/",KabupatenDetail.as_view(),name="detail_kab"),
    path("kecamatan/<int:pk>/",KecamatanDetail.as_view(),name="detail_kec"),
    path("keranjang",KeranjangAPIView.as_view(),name="list_keranjang"),
    path("keranjang/<int:pk>/",KeranjangDetail.as_view(),name="detail_keranjang"),
    path("keranjanguser/<int:user>/",KeranjangUserDetail.as_view(),name="KeranjangUserDetail_list"),
    path("harga/<int:pk>/",HargaDetail.as_view(),name="detail_harga"),
    path("user",RegisterUser.as_view(),name="create_keranjang"),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html', 'api'])