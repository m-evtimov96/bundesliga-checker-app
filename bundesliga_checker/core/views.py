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
        current_team['ShortName'] = team['ShortName']
        current_team['Points'] = team['Points']
        current_team['Goals'] = team['Goals']
        current_team['WonLostDraw'] = won_lost_draw
        current_team['WinLossRatio'] = win_loss_ratio

        teams.append(current_team)

    context = {
        'teams': teams,
    }

    return render(request, 'core/all-teams.html', context)


def team_detail(request, team_short_name):

    teams_data = requests.get('https://www.openligadb.de/api/getbltable/bl1/2021').json()

    team = [team for team in teams_data if team['ShortName'] == team_short_name][0]

    all_matches_data = requests.get('https://www.openligadb.de/api/getmatchdata/bl1/2021').json()

    finished_matches = []
    upcoming_matches = []

    for match in all_matches_data:
        opponent = None
        is_finished = match['MatchIsFinished']

        if match['Team1']['ShortName'] == team_short_name:
            opponent = match['Team2']['TeamName']
            opponent_icon = match['Team2']['TeamIconUrl']
            if is_finished:
                result = f"{match['MatchResults'][0]['PointsTeam1']} : {match['MatchResults'][0]['PointsTeam2']}"

        elif match['Team2']['ShortName'] == team_short_name:
            opponent = match['Team1']['TeamName']
            opponent_icon = match['Team1']['TeamIconUrl']
            if is_finished:
                result = f"{match['MatchResults'][0]['PointsTeam2']} : {match['MatchResults'][0]['PointsTeam1']}"

        if opponent:
            match_time = match['MatchDateTime']
            match_to_save = {'opponent': opponent, 'opponent_icon': opponent_icon, 'result': result,
                             'finished': is_finished, 'date_time': match_time}

            if match_to_save['finished']:
                finished_matches.append(match_to_save)
            else:
                upcoming_matches.append(match_to_save)

    context = {
        'team': team,
        'finished_matches': finished_matches,
        'upcoming_matches': upcoming_matches,
    }

    return render(request, 'core/team.html', context)