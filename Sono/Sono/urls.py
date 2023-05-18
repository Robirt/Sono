from django.urls import path
from django.contrib import admin
from app import views
from django.conf import settings
from django.conf.urls.static import static
from app.controllers import genre_controller, song_controller, album_controller, rental_controller, product_controller, band_controller, band_member_controller


urlpatterns = [
    path('', views.home, name="home"),
    path('catalog/', views.catalog, name='catalog'),
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('admin/', admin.site.urls),
    path('genres/', genre_controller.genres, name='genres'),
    path('songs/', song_controller.songs, name='songs'),
    path('albums/', album_controller.albums, name='albums'),
    path('products/', product_controller.products, name='products'),
    path('rentals/', rental_controller.rentals, name='rentals'),
    path('bands/', band_controller.bands, name='bands'),
    path('band_members/', band_member_controller.band_members, name='band_members'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

