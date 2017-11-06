from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

from . import views

urlpatterns = [
    # == Index: game/
    url(r'^$', views.index, name='index'),

    # == Which player document: game/<>/
    url(r'^(?P<game_id>\d+)/$', views.index, name='index_game'),

    # == GameBoard document (without session): game/<>/player/<>/
    url(r'^(?P<game_id>\d+)/player/(?P<player_id>\d+)/$',
        views.index, name='index_game_player'),

    # == GET board state (without session): game/<>/player/<>/state
    url(r'^(?P<game_id>\d+)/player/(?P<player_id>\d+)/state$',
        views.get_game_state, name='get_game_state'),

    # == POST attack move (without session): game/<>/player/<>/attack
    url(r'^(?P<game_id>\d+)/player/(?P<player_id>\d+)/attack/$',
        views.attack_location, name='attack_location'),

    # == POST alteration (without session): game/<>/player/<>/attack
    # This is essentially unrestricted ATM, which is bad, of course.
    url(r'^(?P<game_id>\d+)/player/(?P<player_id>\d+)/$',
        views.alter_board, name='alter_board'),

    #url(r'new_game', views.new_game, name='new_game'),
    #url(r'join_game', views.join_game, name='join_game'),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()