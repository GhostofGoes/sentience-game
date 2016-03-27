==================
Class Definitions
==================


+++++
Node
+++++


Notes

* Can only belong to a single network or subnet (which is part of a network)

**Members**

*Types*
  Router (We abstract away switches, etc)
  Firewall (This protects network from attacks)
  IDS (Intelligent firewall)
  Host (a basic node, think laptop, workstation, home server)
    Laptop
    Desktop
    Workstation (E.G desktop for work use, generally more powerful)

  Server (A host that is running some service as its primary purpose, such as a website, database, etc)
    Website
    Database
    Login
    Email
    Social Network
    Chat

*Tools*
    List of tools that the node has access to (and you can use if you take over the node)
*Items*
    List of items that the node has (and you acquire if you take over the node)


**Methods**

++++++++
Network
++++++++


**Members**

*Nodes*
    Collection of nodes on the network

*Sysadmins*
    Collection of NPCs associated with the network

*Abilities*
    Collection of abilities the network possesses (could include abilities of nodes as well, but could also just be ones accquired by total control of network)

*Neighbors*
    Collection of networks that are adjacently connected to this network

*Subnets*
    Collection of networks that are "sub" networks (e.g, they're treated the same as nodes)



+++++
Item
+++++


**Members**

*Exploit*
    Classes

        1. Zero-Day
        2. "Patched"
        3. Oracle "Patched"
        4. Skript-kiddie

    Type

        * Email Phishing
        * Chain-letter
        * Backdoor
        * Vulnerability

*Sensitive Data*
    Severity

        1. OPM
        2. Hillary's Emails
        3. CEO's browsing history
        4. Grandma's browsing history




+++++
Tool
+++++


**Members**

*Types*

* X-ploiter
    Exploit tool, used to attack nodes
* Email
    Sends and recieves emails
* Ping
    Pings a host, a basic test of connectivity
* Scan
    Scans a subnet or network and gives a list of all the (visible) nodes or networks on that subnet/network.
    Can be upgraded to be more stealthy, have more information gain, etc.
* SSH
    Connect to a host to send commands and receive data. Your basic "pivot"


**Methods**




++++
NPC
++++


**Members**

(Subclass Person)
    (Subclass Human)
    (Subclass AI)

(Subclass Entity)
    (Subclass Business)
    (Subclass Government)
    (Subclass APT) (because buzzwords yo)


+++++++
Player
+++++++

**Members**

*Inventory*
    List of Items (see item class)


+++++
Game
+++++

**Methods**

new_game(name)
    Creates a new game state with given name

load_game(name)
    Loads a previously saved game state

save_game(name)
    Saves current named game state to disk

start_game(name)
    Starts the game

end_game(name)
    Saves game state, performs cleanup, and exits to main menu

exit()
    Performs cleanup and terminates the application


++++
UI
++++




