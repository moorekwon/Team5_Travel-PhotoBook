from django.urls import path
from photobook import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.album_create, name='album_create'),
    path('page_1/<int:photobook_pk>', views.page_create, name='page_1'),
]
