from django.urls import path
from . import views

urlpatterns = [
    path('', views.allmyblog, name='allmyblog'),
    path('<int:blog_id/>', views.detail, name='detail'),
]
