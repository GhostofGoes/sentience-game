# model.py
# Classes Implementing the core game functionality
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
# along with wsu-hack  If not, see <http://www.gnu.org/licenses/>.


# A collection of nodes, administrators and network resources
class Network(object):
    """A collection of nodes, administrators and network resources"""

    def __init__(self):
        pass


# A node on a network
class Node(object):
    """Represents an object like a host or router"""

    def __init__(self):
        pass


# A tool that can be used by the player
class Tool(object):
    """ TODO """

    def __init__(self):
        pass


# A game item
class Item(object):
    """ TODO """

    def __init__(self):
        pass


# Any non-playable character or entity
class NPC(object):
    """Any non-playable character or entity"""

    def __init__(self):
        pass


# The human-playable character (AI)
class Player(object):
    """A human controlled player (AI)"""

    def __init__(self):
        self.influence = 0
        self.abilities = None

