from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('', Home.as_view(), name='home'),
    re_path(r'^search/$', NavSearch.as_view(), name='catalog'),
    path('catalog/search/', CatalogResults.as_view(), name='searchcatalog'),
    path('catalog/<int:pk>/', Tovar.as_view(), name='tovar'),
    path('catalog/', HomeCatalog.as_view(), name='homecatalog'),
    path('catalog/category=<int:category_id>/', Category.as_view(), name='categorycatalog'),
    path('catalog/brand=<str:brand_title>/', Brand.as_view(), name='brandcatalog'),
]
