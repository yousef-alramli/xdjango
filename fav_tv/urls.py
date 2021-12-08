from django.urls import path
from .views import FavTvListView, FavTvDetailView, FavTvCreateView, FavTvUpdateView, FavTvDeleteView

urlpatterns = [
    path('', FavTvListView.as_view(), name='home'),
    path('<int:pk>/', FavTvDetailView.as_view(), name='fav_tv_detail'),
    path('create/', FavTvCreateView.as_view(), name='fav_tv_create'),
    path('<int:pk>/update/', FavTvUpdateView.as_view(), name='fav_tv_update'),
    path('<int:pk>/delete/', FavTvDeleteView.as_view(), name='fav_tv_delete'),
]