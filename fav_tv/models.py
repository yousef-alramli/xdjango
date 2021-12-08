from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class FavTv(models.Model):
    name = models.CharField(max_length = 30)
    sort = models.CharField(max_length = 20)
    description = models.TextField()
    visitor = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)

    def get_absolute_url (self):
        return reverse ('fav_tv_detail', args=[self.id])
    def __str__(self):
        return self.name