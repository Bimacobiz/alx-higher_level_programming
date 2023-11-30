#!/bin/bash
# obtains, if available, the server's permitted methods using the OPTIONS http request
curl -s -I -X OPTIONS "$1" | grep 'Allow:' | cut -f2- -d' '
