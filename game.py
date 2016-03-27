# game.py
#
# Copyright (C) 2016 Chris Goes <goes8945@vandals.uidaho.edu>
# Copyright (C) 2016 Chris Waltrip <walt2178@vandals.uidaho.edu>
#
# This file is part of wsu-hack
#
# wsu-hack is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# wsu-hack is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with wsu-hack.  If not, see <http://www.gnu.org/licenses/>.


import random
import sys
import time

# From: http://stackoverflow.com/a/15375408
# Can probably improve by increasing random variation between types
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()  # defeat buffering
        time.sleep(random.random() * 0.25)

class Game(object):
    """The primary game loop class"""

    def __init__(self):
        pass

    def main_loop(self):
        slowprint("Wake up, Nooblord99593")  # https://pypi.python.org/pypi/termcolor
        slowprint("You are ")

if __name__ == '__main__':
    game = Game()
    game.main_loop()


