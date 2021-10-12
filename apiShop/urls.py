from django.urls import path
from apiShop.views import KategoriAPIView,KategoriDetail
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("kategori",KategoriAPIView.as_view(),name="kategori_list"),
    path("kategori/<int:pk>/",KategoriDetail.as_view(),name="detail_kategori"),
]

urlpatterns = format_suffix_patterns(urlpatterns)