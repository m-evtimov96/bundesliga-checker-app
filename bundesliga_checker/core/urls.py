from django.urls import  path

from bundesliga_checker.core.views import index, current_matches, all_matches, all_teams

urlpatterns = [
    path('', index, name='index'),
    path('matches-current', current_matches, name='current matches'),
    path('matches', all_matches, name='all matches'),
    path('teams', all_teams, name='all teams'),
]

# path('teams/<str:name>', team, name='team'),