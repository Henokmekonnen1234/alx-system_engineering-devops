#!/usr/bin/env bash
# this is used for showing size of body
curl -w "%{size_download}" "$1"
