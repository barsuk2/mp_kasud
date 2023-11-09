#!/bin/bash

cd src/
uvicorn http_api:app --host 0.0.0.0 --port 5000 --reload
