from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from rest_shop.views import ItemAPIView, CartAPIView, LikeAPIView, LikeDestroyView, LikeCreatetView, AddToCartView, RemoveFromCartView, index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('api/v1/items/', ItemAPIView.as_view()),
    path('api/v1/cart/', CartAPIView.as_view()),
    path('api/v1/like/', LikeAPIView.as_view()),
    path('api/v1/likedelete/<str:item>/', LikeDestroyView.as_view()),
    path('api/v1/likecreate/', LikeCreatetView.as_view()),
    path('api/v1/removefromcart/<str:item>/', RemoveFromCartView.as_view()),
    path('api/v1/addtocart/', AddToCartView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
