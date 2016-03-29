# game.py
#
# Copyright (C) 2016 Chris Goes <goes8945@vandals.uidaho.edu>
# Credit to Chris Waltrip for setting up licence and the idea of using MVC model
#
# This file is part of wsu-hack
#
# sentience-game is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# sentience-game is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with sentience-game.  If not, see <http://www.gnu.org/licenses/>.

import jsonpickle
import random
import sys
import os
import time


# From: http://stackoverflow.com/a/15375408
# Can probably improve by increasing random variation between types
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()  # defeat buffering
        time.sleep(random.random() * 0.25)


# Took a lot of game state loading/saving stuff from: http://stackoverflow.com/a/19744073
class Game(object):

    game_state = dict()

    game_name = "default_game_name"
    save_file_name = "default_save.json"

    wake_up_message = ""  # TODO import from chem notes

    def __init__(self):
        pass

    def new_game(self, name):
        if os.path.isfile(name + ".json"):  # TODO
            print("Game already exists. Are you sure you want to overwrite?")

        self.game_name = name
        self.save_file_name = name + ".json"
        self.initialize_game()
        self.save_game()

    def initialize_game(self):
        pass

    # TODO: keep track of last save user...er, used
    def load_game(self, name):
        self.game_name = name
        self.save_file_name = name + ".json"
        with open(self.save_file_name, 'r') as savegame:
            self.game_state = jsonpickle.decode(savegame.read())

    # Saves the game state to a file
    def save_game(self):
        with open(self.save_file_name, 'w') as savegame:
            savegame.write(jsonpickle.encode(self.game_state))

    def start_game(self):
        pass

    def end_game(self):
        pass

    # Performs cleanup, saving, and terminates the application
    def quit(self):
        self.save_game()
        pass

    def main_loop(self):
        slowprint("Wake up, Nooblord99593")  # https://pypi.python.org/pypi/termcolor
        slowprint("You are ")


def main():
    game = Game()
    game.main_loop()

if __name__ == '__main__':
    # Startup stuff
    # Load UI
    main()



