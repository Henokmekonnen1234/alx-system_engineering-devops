#!/usr/bin/env bash
curl -sw "%{size_download} \n" "$1"
