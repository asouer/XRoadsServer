from flask import Blueprint, request, redirect, url_for, jsonify, render_template
from XRoadsServer.models.CharacterClasses import *
from XRoadsServer.models.Character import Character
from XRoadsServer.models.Utilities import *
from XRoadsServer.models.Weapons import *
from XRoadsServer.models.Backgrounds import *
# from flask_api import status

mod = Blueprint('game', __name__)


@mod.route('/')
def mobile():
    player_one = Character(Athlete(), player_name="Aaron Souer", character_name="Drake",
                           primary_weapon=AssaultRifle(), utility=[AblativePlating()])

    player_one.rank_up()
    player_one.set_character_class(Assault())

    player_two = Character(Scientist(), player_name="Willson Borchert", character_name="Spyndri",
                           primary_weapon=Shotgun())
    player_thr = Character(Scientist(), player_name="Mike Lubke", character_name="Kaine",
                           primary_weapon=Shotgun())
    return render_template('game/game.html', players=[player_one, player_two, player_thr])


@mod.route('/ko')
def game_ko():
    player_one = Character(Athlete(), player_name="Aaron Souer", character_name="Drake",
                           primary_weapon=AssaultRifle(), utility=[AblativePlating()])

    player_one.rank_up()
    player_one.set_character_class(Assault())

    player_two = Character(Scientist(), player_name="Willson Borchert", character_name="Spyndri",
                           primary_weapon=Shotgun())
    player_thr = Character(Scientist(), player_name="Mike Lubke", character_name="Kaine",
                           primary_weapon=Shotgun())
    return render_template('game/game_ko.html', players=[player_one, player_two, player_thr])


@mod.route('/ko2')
def game_ko2():
    return render_template('game/game_ko2.html')


@mod.route('/ko2/api')
def game_ko_api():

    player_one = Character(Athlete(), player_name="Aaron Souer", character_name="Drake",
                           primary_weapon=AssaultRifle(), utility=[AblativePlating()])

    player_one.rank_up()
    player_one.set_character_class(Assault())

    player_two = Character(Scientist(), player_name="Willson Borchert", character_name="Spyndri",
                           primary_weapon=Shotgun())

    game_data = {"players": [player_one.to_dict(), player_two.to_dict()]}

    return jsonify(game_data)
