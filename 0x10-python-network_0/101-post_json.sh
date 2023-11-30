#!/bin/bash
# Will post the JSON data then test the server
curl -s -d "@$2" -H "Content-Type: application/json" -X POST "$1"
