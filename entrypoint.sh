#!/bin/sh

uvicorn main:app --proxy-headers --host 0.0.0.0 --port $PORT --workers 4