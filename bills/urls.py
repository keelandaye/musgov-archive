from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'bills'

urlpatterns = [
    path('', views.index, name='index'),
    path('bill/', views.BillsListView.as_view(), name='list'),
    path('bill/<pk>/', views.BillDetailView.as_view(), name='detail'),
    path('house/', views.HouseListView.as_view(), name='houselist'),
    path('house/<pk>/', views.housedetail, name='housedetail'),
    path('bill/<pk>/edit', login_required(views.BillUpdateView.as_view()), name='billupdate'),
    path('bill/add', login_required(views.BillCreateView.as_view()), name='billcreate'),
    path('house/add', login_required(views.HouseCreateView.as_view()), name='housecreate'),
    path('house/<pk>/edit', login_required(views.HouseUpdateView.as_view()), name='houseupdate'),
    path('bill/<pk>/delete', login_required(views.BillDeleteView.as_view()), name='billdelete'),
    path('house/<pk>/delete', login_required(views.HouseDeleteView.as_view()), name='housedelete'),
    path('bill/search', views.BillSearchListView.as_view(), name='billsearch'),
    path('guide/', login_required(views.guide), name='guide'),
]
