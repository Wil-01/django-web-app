from listings import views
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bands/', views.band_list, name = 'band-list'),
    path('bands/<int:id>/', views.band_detail, name='band-detail'),
    path('bands/add/', views.band_create, name='band-create'),
    path('about-us/', views.about),
    path('contact-us/', views.contact),
    path('listings/', views.listing),
    path('contact-us', views.contact, name='contact'),
    path('email-sent', views.email_sent, name = 'email-sent'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

]
