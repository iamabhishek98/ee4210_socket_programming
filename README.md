# Prerequisites

Python 3.8 libraries: socket, os, sys, urllib

# Running the application

**TCP Server**

Command: `python tcp_server.py`

1. The program will choose the default host address and pick an available port.

2. Using the displayed host address and port upon running the program, access the webpage using a modern browser which supports HTTP1.1.

**UDP Server**

Command: `python udp_server.py`

1. The program will choose the default host address and pick an available port.

2. Using the displayed host address and port upon running the program, send a HTTP1.1 GET request with the help of a networking utility like `netcat` to view the webpage.
