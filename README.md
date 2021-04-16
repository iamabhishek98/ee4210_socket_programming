# EE4210 CA2: Programming Assignment

## Prerequisites

Python 3.5.6 libraries: socket, os, sys, urllib

OS: Ubuntu 20.04

## Running the application

**TCP Server**

Command: `python tcp_server.py`

1. The program will choose the default host address and pick an available port.

2. Using the host address and port displayed upon running the program, access the webpage using a modern browser which supports HTTP/1.1.

**UDP Server**

Command: `python udp_server.py`

1. The program will choose the default host address and pick an available port.

2. Using the host address and port displayed upon running the program, send a HTTP/1.1 GET request with the help of a networking utility like `netcat` to view the webpage.
