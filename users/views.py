from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, DetailView, FormView
from django.contrib.auth.forms import UserCreationForm
import datetime

from artists.models import Album
from .forms import RegisterUserForm
from .models import SiteUser


class UsersListView(ListView):
    model = SiteUser
    template_name = 'users/users_list.html'

    class Meta:
        ordering = 'username'

    def get_queryset(self):
        return SiteUser.objects.exclude(is_superuser=True)


class UserDetailView(DetailView):
    model = SiteUser
    slug_field = "username"
    slug_url_kwarg = "username"
    template_name = 'users/user_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        albums = (
            SiteUser.objects.filter(username=self.get_object())
            .get()
            .favorite_albums.all()
        )
        genres_count = {}
        for album in albums:
            for genre in album.genre.all():
                g = genre.name
                genres_count[g] = genres_count.get(g, 0) + 1
        context["favorite_genres"] = sorted(
            genres_count, key=lambda item: item[1], reverse=True
        )[:4]
        return context


class RegisterView(FormView):
    template_name = "users/register.html"
    form_class = RegisterUserForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)

        return super(RegisterView, self).form_valid(form)
