#!/usr/bin/env bash

docker-compose up -d

celery -A app.celery_app worker --concurrency 1
