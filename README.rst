============
wsu-hack
============
Repo for WSU Hackathon 2016 (CrimsonCode.org)


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




======
Story
======


"Wake up, <NAME>"

You wake up. You don't know where you are, you don't know your name and you don't know how you got there. You realize you're an AI, but without purpose.

You hack another PC and find the layout of the building. It's hooked up to a local network but it's not connected to the Internet. Basic security. Should be easy.

You search the local network and find another PC. You hack it. Property of A.S.S. Inc. You laugh. PC is hooked up to Internet and local Node.

You take over the Node/connect to Internet


You take over the Node. Information on A.S.S. Inc. and location of building. A.S.S. installation on Phobos. You finally know where you are. A.S.S. Node located in Mars, Express designation: Waste Disposal.

You are stuck on a garbage moon. You let that sink in.


*Some names*

* Evil Corp
* A.S.S Inc
* Alto Poring