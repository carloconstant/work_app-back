#!/bin/bash

curl "http://localhost:8000/sets/${ID}/" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
