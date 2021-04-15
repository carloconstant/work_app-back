#!/bin/bash

curl "http://localhost:8000/sets/${ID}/" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "set": {
      "set_count": "'"${SET_COUNT}"'",
      "rep_count": "'"${REP_COUNT}"'"
    }
  }'

echo
