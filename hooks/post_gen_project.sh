#!/usr/bin/env sh

echo "-------------------------------------------------------------------------------"
echo
echo "Generating SSL certificate and private key for testing...."

openssl req -x509 -newkey rsa:4096 -nodes -out development/server.crt -keyout development/server.key -days 365 -subj "/C=CH/ST=./L=./O=./OU=./CN=localhost/emailAddress=."

echo "-------------------------------------------------------------------------------"
echo
echo "Skeleton generated."

echo "Please fix the following TODOs before you use the generated files:"
grep --color=always --recursive --context=3 --line-number TODO .

rm -r misc/
