from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import FavTv


class FavTvListView(ListView):
    template_name = "fav/fav_tv_list.html"
    model = FavTv


class FavTvDetailView(DetailView):
    template_name = "fav/fav_tv_detail.html"
    model = FavTv


class FavTvCreateView(CreateView):
    template_name = "fav/fav_tv_create.html"
    model = FavTv
    fields = ["name" , 'sort', 'description', 'visitor']
    success_url = reverse_lazy("home")



class FavTvUpdateView(UpdateView):
    template_name = "fav/fav_tv_update.html"
    model = FavTv
    fields = ["name" , 'sort', 'description']


class FavTvDeleteView(DeleteView):
    template_name = "fav/fav_tv_delete.html"
    model = FavTv
    success_url = reverse_lazy("home")