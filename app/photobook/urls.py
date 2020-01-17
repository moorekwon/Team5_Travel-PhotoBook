from django.urls import path
from photobook import views
from photobook.views import index

urlpatterns = [
    path('', index, name='index'),
    path('page_1/', views.page, name='page_1'),
]
