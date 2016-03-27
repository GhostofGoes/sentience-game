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

*Tools*: List of tools that the node has access to (and you can use if you take over the node)
*Items*: List of items that the node has (and you accquire if you take over the node)


**Methods**

++++++++
Network
++++++++



+++++
Item
+++++



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



+++++++
Player
+++++++

**Members**

*Inventory*
    List of Items (see item class)


+++++
Game
+++++
