from django.urls import path
from apiShop.views import KategoriAPIView,CreateKategoriAPIView,UpdateKategoriAPIView,DeleteKategoriAPIView

urlpatterns = [
    path("list_kategori",KategoriAPIView.as_view(),name="kategori_list"),
    path("create_kategori/", CreateKategoriAPIView.as_view(),name="create_kategori"),
    path("update_kategori/<int:pk>/",UpdateKategoriAPIView.as_view(),name="update_kategori"),
    path("delete_kategori/<int:pk>/",DeleteKategoriAPIView.as_view(),name="delete_kategori")
]
