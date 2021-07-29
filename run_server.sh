#!/bin/bash
echo "Starting Buencafe server with gunicorn"
gunicorn index:server -b 0.0.0.0:8050