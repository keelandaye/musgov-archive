from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('', views.index, name='index'),
    path('house/', views.houselist, name='houselist'),
    path('house/<ident>', views.housedetail, name='housedetail'),
    path('house/<ident>/', views.housedetail, name='housedetail'),
    path('house/<ident>/bills', views.housebills, name='housebills'),
    path('bill/', views.billlist, name='billlist'),
    path('bill/<house>/<number>', views.billdetail, name='billdetail'),
    path('bill/<name>/', views.billdetail, name='billdetail')
]
