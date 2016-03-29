# model.py
# Classes Implementing the core game functionality
#
# Copyright (C) 2016 Chris Goes <goes8945@vandals.uidaho.edu>
#
# This file is part of sentience-game
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


# A node on a network
class Node(object):
    """Represents an object like a host or router"""

    types = {"Router": "Router", "Firewall": "Firewall", "IDS": "IDS",
             "Host": ["Laptop", "Desktop", "Workstation"],
             "Server": ["Website", "Database", "Login", "Email", "Social Network", "Chat"]
             }
    tools = []  # list of tool instances node has access to
    items = []  # list of item instances node contains

    def __init__(self):
        pass


# A collection of nodes, administrators and network resources
class Network(object):

    nodes = []      # nodes on the network
    subnets = []    # sub-networks for this network
    neighbors = []  # the network's neighboring networks
    admins = []     # admins associated with the network
    abilities = []  # Abilities the network possesses

    def __init__(self):
        pass


# A game item
class Item(object):
    """ TODO """

    def __init__(self):
        pass


# A tool that can be used by the player
class Tool(object):
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

    commands = dict()

    def __init__(self):
        self.influence = 0
        self.abilities = None

