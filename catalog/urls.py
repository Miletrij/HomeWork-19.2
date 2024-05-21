from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ContactsTemplateView, HomeListView, ProductDetailView, ProductListView, CategoryListView, \
    CategoryDetailView, ProductDeleteView, ProductCreateView, ProductUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeListView.as_view(), name='homelist'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('catalog/<int:pk>/', ProductDetailView.as_view(), name='product_view'),
    path('products/', ProductListView.as_view(), name='product'),
    path('categorys/', CategoryListView.as_view(), name='category'),
    path('categorys/<slug:pk>/', CategoryDetailView.as_view(), name='category_view'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update'),
]
