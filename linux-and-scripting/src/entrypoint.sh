#!/bin/bash

yes | rm "$0"

echo "bearshell{the-server-is-always-listening}" | nc -l 31337 &

bash
