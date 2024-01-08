#!/bin/sh

set -m

cd /src/example-site && python3 server.py 8000 &
cd /src/challenge-site && python3 server.py 8001 &
cd /src/http-server && python3 server.py 8002
