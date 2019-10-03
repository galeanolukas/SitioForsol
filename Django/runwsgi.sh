#!/bin/bash
uwsgi --tcp-nodelay  --wsgi-file wsgi.py --enable-threads --socket 127.0.0.1:3030
 
