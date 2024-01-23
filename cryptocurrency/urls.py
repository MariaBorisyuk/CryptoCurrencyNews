from django.urls import path, include
from .views import index, show_crypto_currency_news, add_cryptocurrency, NewsViewSet, CryptoCurrencyViewSet, show_test_api
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('news', NewsViewSet, basename='news')
router.register('crypto_currency', CryptoCurrencyViewSet, basename='crypto_currency')

urlpatterns = [
    path('', index),
    path('news/<int:currency_id>/', show_crypto_currency_news),
    path('add_cryptocurrency/', add_cryptocurrency),
    path('api/', include(router.urls)),
    path('show_test_api/', show_test_api)
]
