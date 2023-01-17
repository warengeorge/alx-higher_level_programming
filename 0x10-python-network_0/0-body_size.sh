#!/bin/bash
# Take url, send request, display size of body
curl -s "$1" | wc -c
