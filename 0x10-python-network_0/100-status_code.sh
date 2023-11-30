#!/bin/bash
# Displays the status code of a server
curl -L -s -X HEAD -w "%{http_code}" "$1"
