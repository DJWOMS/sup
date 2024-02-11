#!/bin/sh

alembic upgrade head

uvicorn src.main:app --reload --host "0.0.0.0" --port "8000" --log-level "debug" --use-colors
