from django.urls import path
from photobook import views

urlpatterns = [
    path('page_1/', views.page, name='page_1')
]
