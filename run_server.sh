#!/bin/bash
echo "Starting Buencafe server with gunicorn"
gunicorn app:server -b 0.0.0.0:8050