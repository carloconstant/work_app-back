#!/bin/bash

curl "http://localhost:8000/sets/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
