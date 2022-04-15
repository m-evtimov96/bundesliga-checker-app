from django.shortcuts import render
from django.views.decorators.http import require_GET
import requests

def index(request):

    return render(request, 'core/index.html')


@require_GET
def current_matches(request):

    response = requests.get('https://www.openligadb.de/api/getmatchdata/bl1/')
    current_matches_data = response.json()

    context = {
        'matches': current_matches_data,
    }

    return render(request, 'core/current-matches.html', context)


@require_GET
def all_matches(request):

    response = requests.get('https://www.openligadb.de/api/getmatchdata/bl1/2021')
    all_matches_data = response.json()

    context = {
        'matches': all_matches_data,
    }

    return render(request, 'core/all-matches.html', context)


@require_GET
def all_teams(request):

    response = requests.get('https://www.openligadb.de/api/getbltable/bl1/2021')
    response_data = response.json()

    teams = []
    for team in response_data:
        current_team = {}

        won_lost_draw = str(team['Won']) + '-' + str(team['Lost']) + '-' + str(team['Draw'])
        win_loss_ratio = team['Won'] / team['Lost']
        win_loss_ratio = f'{win_loss_ratio:.3f}'

        current_team['Icon'] = team['TeamIconUrl']
        current_team['Name'] = team['TeamName']
        current_team['Points'] = team['Points']
        current_team['Goals'] = team['Goals']
        current_team['WonLostDraw'] = won_lost_draw
        current_team['WinLossRatio'] = win_loss_ratio

        teams.append(current_team)

    context = {
        'teams': teams,
    }

    return render(request, 'core/all-teams.html', context)