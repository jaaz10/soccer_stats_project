from django.shortcuts import render

from .models import Player, Team


def home(request):
    return render(request, "player_tracker/home.html")


def team_list(request):
    teams = Team.objects.all()
    return render(request, "player_tracker/team_list.html", {"teams": teams})


def player_list(request):
    players = Player.objects.all()
    return render(request, "player_tracker/player_list.html", {"players": players})
